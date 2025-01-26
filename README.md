# [CHART ASIST: Team Coordination Analysis](https://somwrks.notion.site/CHART-ASIST-161e4acf846e8024823ceb2e1bd9a278?pvs=4)

*Repository for analyzing human-AI team coordination in Minecraft-based search-and-rescue tasks.*

---

## 📂 Repository Structure
```
CHART_ASIST/  
├── .venv/                  # Python virtual environment (dependencies)
├── Study3_Analysis/        # Core analysis workflows and data
│   ├── data/               # Raw datasets (JSON logs, surveys, videos)
│   ├── processed/          # Cleaned data and analysis outputs
│   ├── scripts/            # Jupyter notebooks and Python scripts
│   └── README.md           # Detailed project documentation
└── README.md               # This file (overview)
```

---

## 🚀 Getting Started
1. **Clone this repository**:
   ```bash
   git clone https://github.com/yourusername/CHART-ASIST.git
   cd CHART-ASIST
   ```

2. **Set up the virtual environment**:
   ```bash
   source .venv/bin/activate  # Linux/WSL
   # .venv\Scripts\activate  # Windows
   ```

3. **Navigate to the analysis folder**:
   ```bash
   cd Study3_Analysis
   ```

4. **Follow detailed instructions** in [Study3_Analysis/README.md](Study3_Analysis/README.md) for:
   - Data preprocessing
   - Statistical analysis
   - Visualization workflows

---

## 🔍 Key Components
| Folder/File           | Purpose                                                                 |
|-----------------------|-------------------------------------------------------------------------|
| `.venv/`              | Contains Python dependencies (`opencv-python`, `pandas`, `scipy`, etc.)|
| `Study3_Analysis/`    | Main analysis workflows (Jupyter notebooks, data, results)             |
| `Study3_Analysis/data`| Raw datasets from ASIST Study 3 (JSON logs, SPSS surveys, videos)      |

---

## 🛠 Requirements
- Python 3.10+
- WSL (Windows Subsystem for Linux) recommended for Linux-like environment
- Jupyter Lab for interactive analysis

---

## 📈 Analysis Workflow
1. **Data Parsing**  
   Convert raw JSON/SPSS/VTT files to structured CSVs.  
2. **Multi-Modal Analysis**  
   Correlate AI advice patterns (`advice_type`, `timestamp`) with team outcomes (`game_score`).  
3. **Visualization**  
   Generate plots showing relationships between variables (e.g., Seaborn boxplots).

---
