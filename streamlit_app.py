
import streamlit as st

from storage import load_experiments, save_experiments
from llm import generate_response

from experiment import (
    create_experiment,
    calculate_statistics,
    rank_experiments,
    evaluate_experiments,
    find_experiment_by_version,
    filter_experiments_by_evaluation,
    validate_experiment_details,
    validate_score,
    find_best_experiment
)

from database import delete_experiment_from_db

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="PromptTrace",
    page_icon="🧪",
    layout="wide"
)

# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown("""
<style>

.stApp {
    background-color: #f5f7fb;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
    max-width: 1200px;
}

[data-testid="stSidebar"] {
    background-color: #111827;
}

[data-testid="stSidebar"] * {
    color: white;
}

div[data-testid="stMetric"] {
    background-color: white;
    padding: 18px;
    border-radius: 12px;
    border: 1px solid #e5e7eb;
}

.stButton button {
    border-radius: 8px;
    font-weight: 600;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# SESSION STATE
# --------------------------------------------------

if "pending_experiment" not in st.session_state:
    st.session_state.pending_experiment = None

if "save_message" not in st.session_state:
    st.session_state.save_message = None

# --------------------------------------------------
# HELPER FUNCTION
# --------------------------------------------------

def get_experiments():

    try:
        return load_experiments()

    except Exception as error:
        st.error(f"Database error: {error}")
        return []

def show_experiment_table(experiments):

    if not experiments:
        st.info("No experiments found.")
        return

    rows = []

    for experiment in experiments:

        rows.append({
            "Version": experiment["prompt_version"],
            "Task": experiment["task"],
            "Model": experiment["model"],
            "Score": experiment["score"],
            "Evaluation": (
                "Good Score"
                if experiment["score"] >= 7
                else "Needs Improvement"
            )
        })

    st.dataframe(
        rows,
        use_container_width=True,
        hide_index=True
    )

# --------------------------------------------------
# SIDEBAR NAVIGATION
# --------------------------------------------------

st.sidebar.title("🧪 PromptTrace")

st.sidebar.caption("GenAI Experiment Workspace")

page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "New Experiment",
        "Experiment History",
        "Search & Filter",
        "Compare Prompts",
        "Delete Experiment"
    ]
)

st.sidebar.divider()

st.sidebar.caption("PromptTrace | GenAI Workspace")

# --------------------------------------------------
# DASHBOARD
# --------------------------------------------------

if page == "Dashboard":

    st.title("Dashboard")

    st.caption(
        "Monitor your prompt experiments and performance."
    )

    experiments = get_experiments()

    stats = calculate_statistics(experiments)

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Total Experiments",
        stats["total"]
    )

    col2.metric(
        "Average Score",
        f'{stats["average"]:.2f}'
    )

    col3.metric(
        "Highest Score",
        stats["highest"]
    )

    col4.metric(
        "Lowest Score",
        stats["lowest"]
    )

    st.divider()

    st.subheader("Experiment Score Overview")

    if experiments:

        chart_data = {
            experiment["prompt_version"]: experiment["score"]
            for experiment in experiments
        }

        st.bar_chart(chart_data)

        st.subheader("Experiment Rankings")

        ranked = rank_experiments(experiments)

        evaluations = evaluate_experiments(ranked)

        rows = []

        previous_score = None
        current_rank = 0

        for position, (experiment, evaluation) in enumerate(
            zip(ranked, evaluations),
            start=1
        ):

            score = experiment["score"]

            if score != previous_score:
                current_rank = position

            rows.append({
                "Rank": current_rank,
                "Version": experiment["prompt_version"],
                "Model": experiment["model"],
                "Score": score,
                "Evaluation": evaluation
            })

            previous_score = score

        st.dataframe(
            rows,
            use_container_width=True,
            hide_index=True
        )

        best = find_best_experiment(experiments)

        if best:
            st.success(
                f'Best Experiment: {best["prompt_version"]} '
                f'with score {best["score"]}/10'
            )

    else:
        st.info("Create your first experiment to see dashboard data.")

# --------------------------------------------------
# NEW EXPERIMENT
# --------------------------------------------------

elif page == "New Experiment":

    st.title("Create New Experiment")

    st.caption(
        "Generate an AI response and evaluate its quality."
    )

    with st.form("new_experiment_form"):

        task = st.text_input(
            "Task Name",
            placeholder="Example: GenAI Testing"
        )

        prompt = st.text_area(
            "Enter Your Prompt",
            placeholder="Write your prompt here...",
            height=150
        )

        prompt_version = st.text_input(
            "Prompt Version",
            placeholder="Example: v6"
        )

        submitted = st.form_submit_button(
            "Generate Gemini Response",
            use_container_width=True
        )

    if submitted:

        validation_error = validate_experiment_details(
            task,
            prompt,
            prompt_version
        )

        if validation_error:

            st.error(validation_error)

        else:

            experiments = get_experiments()

            duplicate = any(
                e["prompt_version"] == prompt_version
                for e in experiments
            )

            if duplicate:

                st.error("This prompt version already exists.")

            else:

                try:

                    with st.spinner("Generating Gemini response..."):

                        response = generate_response(prompt)

                    st.session_state.pending_experiment = {
                        "task": task,
                        "prompt": prompt,
                        "prompt_version": prompt_version,
                        "response": response
                    }

                except Exception as error:

                    st.error(
                        "Gemini API request failed. "
                        "Please try again later."
                    )

                    st.caption(str(error))

    pending = st.session_state.pending_experiment

    if pending:

        st.divider()

        st.subheader("Generated Gemini Response")

        st.markdown(pending["response"])

        st.divider()

        score = st.slider(
            "Rate this response",
            min_value=1,
            max_value=10,
            value=7,
            key="experiment_score"
        )

        if st.button(
            "Save Experiment",
            use_container_width=True
        ):

            validation_error = validate_score(score)

            if validation_error:

                st.error(validation_error)

            else:

                new_experiment = create_experiment(
                    pending["task"],
                    pending["prompt"],
                    pending["prompt_version"],
                    "Gemini",
                    pending["response"],
                    score
                )

                saved = save_experiments([new_experiment])

                if saved:

                    st.session_state.save_message = (
                        f'Experiment {pending["prompt_version"]} '
                        "saved successfully!"
                    )

                    st.session_state.pending_experiment = None

                    st.rerun()

                else:

                    st.error(
                        "Experiment could not be saved. "
                        "Check for a duplicate version."
                    )

    if st.session_state.save_message:

        st.success(st.session_state.save_message)

        st.session_state.save_message = None

# --------------------------------------------------
# EXPERIMENT HISTORY
# --------------------------------------------------

elif page == "Experiment History":

    st.title("Experiment History")

    experiments = get_experiments()

    st.write(
        f"Total saved experiments: {len(experiments)}"
    )

    show_experiment_table(experiments)

    if experiments:

        with st.expander("View prompt and response details"):

            for experiment in experiments:

                st.subheader(
                    experiment["prompt_version"]
                )

                st.write("Task:", experiment["task"])

                st.write("Prompt:", experiment["prompt"])

                st.write("Response:")

                st.markdown(experiment["response"])

                st.write("Score:", experiment["score"])

                st.divider()

# --------------------------------------------------
# SEARCH AND FILTER
# --------------------------------------------------

elif page == "Search & Filter":

    st.title("Search & Filter")

    experiments = get_experiments()

    st.subheader("Search by Prompt Version")

    version = st.text_input(
        "Enter Prompt Version",
        placeholder="Example: v2"
    )

    if st.button("Search Experiment"):

        if not version.strip():

            st.warning("Enter a prompt version.")

        else:

            result = find_experiment_by_version(
                experiments,
                version.strip()
            )

            if result:

                st.success("Experiment Found!")

                show_experiment_table([result])

            else:

                st.error("Experiment Not Found!")

    st.divider()

    st.subheader("Filter by Evaluation")

    evaluation = st.selectbox(
        "Select Evaluation",
        [
            "Good Score",
            "Needs Improvement"
        ]
    )

    if st.button("Apply Filter"):

        filtered = filter_experiments_by_evaluation(
            experiments,
            evaluation
        )

        show_experiment_table(filtered)

# --------------------------------------------------
# COMPARE PROMPTS
# --------------------------------------------------

elif page == "Compare Prompts":

    st.title("Compare Prompt Versions")

    experiments = get_experiments()

    if len(experiments) < 2:

        st.info("At least two experiments are required.")

    else:

        versions = [
            e["prompt_version"]
            for e in experiments
        ]

        selected_versions = st.multiselect(
            "Select experiments to compare",
            versions,
            default=versions[:2]
        )

        if len(selected_versions) >= 2:

            selected = [
                e for e in experiments
                if e["prompt_version"] in selected_versions
            ]

            show_experiment_table(selected)

            scores = [
                e["score"] for e in selected
            ]

            st.metric(
                "Score Difference",
                max(scores) - min(scores)
            )

            for experiment in selected:

                with st.expander(
                    f'View {experiment["prompt_version"]} prompt'
                ):

                    st.write(experiment["prompt"])

                    st.write("Response:")

                    st.markdown(experiment["response"])

# --------------------------------------------------
# DELETE EXPERIMENT
# --------------------------------------------------

elif page == "Delete Experiment":

    st.title("Delete Experiment")

    experiments = get_experiments()

    if not experiments:

        st.info("No experiments available.")

    else:

        versions = [
            e["prompt_version"]
            for e in experiments
        ]

        selected_version = st.selectbox(
            "Select Prompt Version",
            versions
        )

        confirm = st.checkbox(
            "I confirm that I want to delete this experiment."
        )

        if st.button(
            "Delete Experiment",
            type="primary"
        ):

            if not confirm:

                st.warning("Please confirm before deleting.")

            else:

                result = delete_experiment_from_db(
                    selected_version
                )

                if result:

                    st.success(
                        f"Experiment {selected_version} deleted."
                    )

                    st.rerun()

                else:

                    st.error("Experiment could not be deleted.")