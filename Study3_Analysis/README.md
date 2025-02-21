# [ASIST Study 3: Multi-Modal Team Performance Analysis](https://somwrks.notion.site/Research-Study-3-Analysis-187e4acf846e80cd881bd3ca4779b465?pvs=4)

## 📌 Objective

Analyze **AI-human team coordination** in a Minecraft-based search-and-rescue mission using multi-modal data:
# Multi-Modal Data Analysis Workflow

**ASIST Study 3 Dataset**

#### **Team 000315 Pre-Result Analysis**

Engineer exibited poor skill during the hands on training. It took him a very long time to complete the individual training which resulted in the mission timer running out during the team training section. Once the timer expired, the hands-on training trial was restarted and participants again completed the individual training. Engineer's second attempt still took over 5 minutes to complete individual training. The competency test was then started at 13m remaining on the timer, the engineer took a full 5 minutes to complete the competency test. Experiment team decided that engineer should be allowed to proceed to avoid rescheduling dispite the evident lack of minecraft skill.

## Objective

Analyze team performance data across four modalities:

1. JSON behavior logs
2. Video recordings
3. Chat transcripts

Identify correlations between AI interventions and team outcomes.

## Note

All datasets were taken from official CHART ASIST Study 3 Dataset available at ASU official repository.

#### Subset used :

| Team ID | ASI ID        | trial   | intervention_recipent     |
| ------- | ------------- | ------- | ------------------------- |
| 000315  | ASI-CMURI-TA1 | T000829 | E001211, E001215, E001155 |



**AI Agent Action signals** -

1. RemindTransporterBeep
2. InformAboutTriagedVictim
3. RemindMedicToInformAboutTriagedVicti
4. TriageCriticalVictim
5. EvacuateCriticalVictim
6. EncouragePlayerProximityToMedicIHMCDyad
7. RemindChangeMarke
8. RemindRubblePerturbatio
9. EvacuationZoneDistanc
10. TeamSawVictimMarke
11. TimeElapse
12. StartEvacuatio

**Agents location**-

1. Location of the agent in the map -> Room Name

**Agent Action**-

1. Transporting victims
2. Performing their role task including stabilizing victims
3. wakening up critical victims
4. placing marking block-> Regular, A, B, C
5. placing marking block for threat rooms
6. removing rubbles
7. detecting victims

## V1 Dataframe

Timestamp, AI Message, AI Action Class, Transporter Message, Engineer Message, Medic Message is extracted from transcript.csv

We use Multimodal LLM analysis to analyze video data to give states and locations of agents + victims throughout the experiment

States tells us what the agent is doing
Locations tells use where the agent is located in the map

| Time Stamp | Asi Message | Asi Action Class | Transporter Message | Engineer Message | Medic Message | Transporter State | Engineer State | Medic State | Transporter location | Engineer location | Medic location | Victim Location |
| ---------- | ----------- | ---------------- | ------------------- | ---------------- | ------------- | ----------------- | -------------- | ----------- | -------------------- | ----------------- | -------------- | --------------- |
| 11:23:01   | N/A         | N/A              | N/A                 | N/A              | N/A           | N/A               | N/A            | N/A         | N/A                  | N/A               | N/A            | N/A             |

## Final Dataframe

States and locations are fused together using LLM analysis to form one action_state column signifying their role in a situation

| timestamp | asi_reason | asi_action | transporter_message | engineer_message | medic_message | transporter_action_state | engineer_action_state | medic_action_state | victim_location | 
| --------- | --------- | --------- | ------------------ | --------------- | ------------ | --------------- | --------------- | ------------ | --------------- |
|           |           |           |                    |                 |              |                 |                 |              |                 |


We then utilize another LLM to finally provide ASI Advice score and team score for their actions and LLM's reasoning behiind that

| timestamp | asi_reason | asi_action | transporter_message | engineer_message | medic_message | transporter_action_state | engineer_action_state | medic_action_state | victim_location | team_score | asi_advice_score |
| --------- | --------- | --------- | ------------------ | --------------- | ------------ | --------------- | ---------- | --------------- | --------------- |--------------- |--------------- |
|     22:03      |   You guys should do [asi_action_class] because...        | 1. RemindTransporterBeep <br/>2. InformAboutTriagedVictim <br/>3. RemindMedicToInformAboutTriagedVicti <br/>4. TriageCriticalVictim <br/>5. EvacuateCriticalVictim <br/>6.EncouragePlayerProximityToMedicIHMCDyad <br/>7. RemindChangeMarke <br/>8. RemindRubblePerturbatio <br/>9. EvacuationZoneDistanc <br/>10. TeamSawVictimMarke <br/>11. TimeElapse <br/>12. StartEvacuatio|     I'm coming for you medic               |     This is more important               |     I can't help you!               |     Carrying a victim from b4 to g4 room               |     Clearing rubbles in threat room for medic  at a9 room          |     waking up critical victim at g5 room        |    next to medic, far from engineer, close to transporter            |  40%          |     75%           |


## AI Instruct Modal

We finetune pretrained LLM on our data for understanding minecraft test bed for asist thoroughly and deeply. Then we utilize it to perform-

1. **Multimodal DataAnalysis of Video Data** 

To give information about agent locations and their actions

2. **Text Fusion Data Analysis**

To fuse meanings and relationships between agent communication, their location and state in given situations to a single column

3. **Scoring Analysis**

To score humans and ASI's advice on team work communication and collaboration data   

