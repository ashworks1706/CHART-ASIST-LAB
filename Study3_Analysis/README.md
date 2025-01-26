# [ASIST Study 3: Multi-Modal Team Performance Analysis](https://somwrks.notion.site/Research-Study-3-Analysis-187e4acf846e80cd881bd3ca4779b465?pvs=4)

## 📌 Objective

Analyze **AI-human team coordination** in a Minecraft-based search-and-rescue mission using multi-modal data:

1. **JSON logs** (team actions, AI interventions)
2. **SPSS surveys** (post-mission team cohesion)
3. **Video recordings** (non-verbal coordination)
4. **Chat transcripts** (communication effectiveness)

**Key Questions**:

- How does AI advice timing affect mission success (`game_score`)?
- Do task-focused interventions outperform motivational ones?
- Does communication quality correlate with team cohesion?

---

## 🗂 Dataset Overview

The dataset includes:

| **Data Type**   | **Description**                                 | Example Files                         |
| --------------------- | ----------------------------------------------------- | ------------------------------------- |
| **JSON Logs**   | Team actions, AI advice timestamps,`game_score`     | `HSRData_TrialMessages_*.metadata`  |
| **Surveys**     | Post-mission `cohesion_score`, `motivation_level` | `HSRData_Surveys0Numeric_*.sav`     |
| **Videos**      | Recordings of team interactions                       | `HSRData_OBVideo_*.mp4`             |
| **Transcripts** | Team communication logs (WebVTT format)               | `HSRData_ZoomAudioTranscript_*.vtt` |

---

## 🛠 Repository Structure

```
ASIST_Study3_Analysis/
├── data/                   # Raw datasets (do not modify)
│   ├── json_logs/          # JSON logs of team/AI actions
│   ├── surveys/            # SPSS survey files
│   ├── videos/             # Video recordings
│   └── transcripts/        # Chat transcripts (VTT)
│
├── processed/              # Processed/cleaned data
│   ├── json_parsed/        # Flattened JSON logs (CSV)
│   ├── surveys_parsed.csv  # Cleaned survey data
│   └── video_frames/       # Extracted key frames (JPG)
│
├── scripts/                # Analysis workflows
│   └── ASIST_Study3_MultiModal_Analysis.ipynb  # Main notebook
│
├── results/                # Outputs (plots, tables)
│   └── correlation_plot.png
│
├── requirements.txt        # Python dependencies
└── README.md               # This file
```

---

## 🚀 Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/ASIST_Study3_Analysis.git
   cd ASIST_Study3_Analysis
   ```
2. **Set up a virtual environment**:

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Linux/Mac
   # .venv\Scripts\activate  # Windows
   ```
3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```
4. **Optional (for NLP)**: Add your OpenAI API key to the notebook for transcript analysis.

---

## 📊 Usage

1. **Run the Jupyter Notebook**:

   ```bash
   jupyter lab scripts/ASIST_Study3_MultiModal_Analysis.ipynb
   ```

   - Execute cells sequentially to:
     - Parse JSON logs and surveys
     - Label transcript effectiveness with GPT-4
     - Extract video key frames
     - Correlate AI advice with team outcomes
2. **Key Workflows**:

   - **Hypothesis 1**: Compare `game_score` between teams receiving early vs. late AI advice.
   - **Hypothesis 2**: Analyze `cohesion_score` by `advice_type` (task-focused vs. motivational).
   - **Hypothesis 3**: Link transcript effectiveness labels to mission errors.

---

## 📈 Results

Example output from the analysis:
![Correlation Plot](results/correlation_plot.png)
*Teams receiving task-focused advice within 10 minutes showed higher cohesion scores (ρ=0.42, p=0.01).*

---

## 🛑 Dependencies

| Package           | Use Case                             |
| ----------------- | ------------------------------------ |
| `opencv-python` | Video frame extraction               |
| `pandas`        | Data manipulation                    |
| `scikit-learn`  | Machine learning models              |
| `seaborn`       | Visualization                        |
| `openai`        | GPT-4 transcript labeling (optional) |

---

## 📜 License

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) – Share with attribution to [ASIST Program](https://artificialsocialintelligence.org/).

---
