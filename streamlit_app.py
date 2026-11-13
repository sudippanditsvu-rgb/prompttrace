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
# SESSION STATE
# --------------------------------------------------

if "pending_experiment" not in st.session_state:
    st.session_state.pending_experiment = None

if "save_message" not in st.session_state:
    st.session_state.save_message = None

if "theme_mode" not in st.session_state:
    st.session_state.theme_mode = "System"

st.sidebar.title("🧪 PromptTrace")
st.sidebar.caption("Created by Sudip Pandit")
st.sidebar.caption("GenAI Experiment Workspace")

theme_mode = st.sidebar.selectbox(
    "Appearance",
    ["System", "Light", "Dark"],
    key="theme_mode"
)

light_variables = """
    --text-color: #1f2937;
    --background-color: #f5f7fb;
    --secondary-background-color: #ffffff;
    --primary-color: #2563eb;
    --button-text-color: #ffffff;
    --border-color: #e5e7eb;
    --muted-color: #6b7280;
    color-scheme: light;
"""

dark_variables = """
    --text-color: #e5e7eb;
    --background-color: #0b1220;
    --secondary-background-color: #111827;
    --primary-color: #60a5fa;
    --button-text-color: #0b1220;
    --border-color: #374151;
    --muted-color: #9ca3af;
    color-scheme: dark;
"""

if theme_mode == "System":
    theme_variables = f"""
    .stApp {{
        {light_variables}
    }}

    @media (prefers-color-scheme: dark) {{
        .stApp {{
            {dark_variables}
        }}
    }}
    """
else:
    selected_variables = (
        dark_variables if theme_mode == "Dark" else light_variables
    )
    theme_variables = f".stApp {{ {selected_variables} }}"

# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown(f"""
<style>

{theme_variables}

.stApp {{
    color: var(--text-color);
    background-color: var(--background-color);
}}

[data-testid="stHeader"] {{
    background-color: var(--background-color);
}}

.block-container {{
    padding-top: 2rem;
    padding-bottom: 2rem;
    max-width: 1440px;
}}

[data-testid="stSidebar"] {{
    background-color: #111827;
}}

[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] *,
[data-testid="stSidebar"] [data-testid="stWidgetLabel"],
[data-testid="stSidebar"] label[data-testid="stRadioOption"] {{
    color: #f9fafb;
}}

div[data-testid="stMetric"] {{
    background-color: var(--secondary-background-color);
    padding: 18px;
    border-radius: 12px;
    border: 1px solid var(--border-color);
}}

div[data-testid="stMetric"] [data-testid="stMetricLabel"],
div[data-testid="stMetric"] [data-testid="stMetricValue"] {{
    color: var(--text-color);
}}

[data-testid="stMain"] [data-testid="stWidgetLabel"],
[data-testid="stMain"] [data-testid="stWidgetLabel"] p {{
    color: var(--text-color) !important;
}}

[data-testid="stMain"] input:not([type="checkbox"]):not([type="radio"]),
[data-testid="stMain"] textarea,
[data-testid="stMain"] [role="combobox"],
[data-testid="stMain"] div[data-baseweb="input"],
[data-testid="stMain"] div[data-baseweb="input"] > div,
[data-testid="stMain"] div[data-baseweb="textarea"],
[data-testid="stMain"] div[data-baseweb="select"] {{
    color: var(--text-color) !important;
    background-color: var(--secondary-background-color) !important;
    border-color: var(--border-color) !important;
}}

[data-testid="stMain"] input::placeholder,
[data-testid="stMain"] textarea::placeholder {{
    color: var(--muted-color) !important;
    opacity: 1;
}}

[data-testid="stMultiSelect"] [role="group"] {{
    background-color: var(--secondary-background-color) !important;
    border-color: var(--border-color) !important;
}}

[data-testid="stMultiSelectTagsContainer"] > span > span {{
    color: var(--button-text-color) !important;
    background-color: var(--primary-color) !important;
    border-color: var(--primary-color) !important;
}}

[data-testid="stMultiSelectTagsContainer"] button {{
    color: var(--button-text-color) !important;
}}

[data-testid="stProgressBarTrack"] {{
    background-color: var(--border-color) !important;
}}

[data-testid="stProgressBarTrack"] > div {{
    background-color: var(--primary-color) !important;
}}

[role="listbox"] {{
    color: var(--text-color);
    background-color: var(--secondary-background-color);
}}

[role="option"] {{
    color: var(--text-color);
}}

div[data-testid="stVerticalBlockBorderWrapper"] {{
    background-color: var(--secondary-background-color);
    border-color: var(--border-color);
}}

[data-testid="stMain"] .stButton button,
[data-testid="stMain"] button[data-testid^="stBaseButton"] {{
    border-radius: 8px;
    font-weight: 600;
    color: var(--button-text-color) !important;
    background-color: var(--primary-color) !important;
    border-color: var(--primary-color) !important;
}}

[data-testid="stMain"] .stButton button:hover,
[data-testid="stMain"] button[data-testid^="stBaseButton"]:hover {{
    filter: brightness(0.95);
}}

.stApp,
[data-testid="stSidebar"],
div[data-testid="stMetric"],
div[data-testid="stVerticalBlockBorderWrapper"] {{
    transition: background-color 180ms ease, color 180ms ease, border-color 180ms ease;
}}

</style>
""", unsafe_allow_html=True)

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

    for experiment in experiments:
        evaluation = (
            "Good Score"
            if experiment["score"] >= 7
            else "Needs Improvement"
        )

        with st.container(border=True):
            version_col, score_col = st.columns([3, 1])
            version_col.markdown(f'**{experiment["prompt_version"]}**')
            score_col.markdown(f'**Score: {experiment["score"]}/10**')

            task_col, model_col, evaluation_col = st.columns([2, 1, 2])
            task_col.caption(f'Task: {experiment["task"]}')
            model_col.caption(f'Model: {experiment["model"]}')
            evaluation_col.caption(evaluation)

# --------------------------------------------------
# SIDEBAR NAVIGATION
# --------------------------------------------------

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

    if experiments:

        for experiment in experiments:
            score = max(0, min(10, int(experiment["score"])))
            st.progress(
                score * 10,
                text=f'{experiment["prompt_version"]} — {score}/10'
            )

        st.subheader("Experiment Rankings")

        ranked = rank_experiments(experiments)

        evaluations = evaluate_experiments(ranked)

        previous_score = None
        current_rank = 0

        for position, (experiment, evaluation) in enumerate(
            zip(ranked, evaluations),
            start=1
        ):

            score = experiment["score"]

            if score != previous_score:
                current_rank = position

            with st.container(border=True):
                rank_col, version_col, score_col = st.columns([1, 3, 1])
                rank_col.caption(f"Rank {current_rank}")
                version_col.markdown(
                    f'**{experiment["prompt_version"]}**'
                )
                score_col.markdown(f"**{score}/10**")

                model_col, evaluation_col = st.columns(2)
                model_col.caption(f'Model: {experiment["model"]}')
                evaluation_col.caption(evaluation)

            previous_score = score

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