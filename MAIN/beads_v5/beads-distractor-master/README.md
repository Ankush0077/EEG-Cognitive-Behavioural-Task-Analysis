#### *Table of contents*
- [BEADS Distractor](#beads-distractor)
    * [Development](#development)
        + [Built with](#built-with)
        + [Prerequisites](#prerequisites)
        + [How to use?](#how-to-use)
    * [Features](#features)
    * [Code Reference](#code-reference)
    * [Code Example](#code-example)
    * [Outputs](#outputs)
    * [Contribute](#contribute)
    * [Authors and acknowledgment](#authors-and-acknowledgment)
    * [License](#license)
    * [References](#references)
# BEADS Distractor

###### tags: `Cognitive bias, Beads task, Jumping to conclusions, Repeated measures, Repeatability, Reliability, Psychosis, Psychopy, Pavlovia`

> Cognitive task to measure the jumping to conclusions bias (JTC).

BEADS Distractor is a cognitive task designed to measure the jumping to conclusions bias (JTC) [[1]](#1) in which some people gather little information before making a decision. Respondents must draw beads from an undisclosed jar and decide which jar is being drawn from once they feel they have gathered enough information. They are then asked to rate their confidence in their decision.

This version was inspired by the "distractor beads" task by McLean et al. [[1]](#1) and can be completed in English and French with repeated administrations. It consists of 21 trials. There is no practice since the first trial serves as the traditional beads trial. 

<p align="center">
<img src="https://gitlab.pavlovia.org/crispstudies/beads-distractor/raw/master/documentation/beads.gif" width="70%" height="70%"/>
</p>

## Development
### Built with
Psychopy software using [Psychopy builder](https://www.psychopy.org/builder) with Javascript custom code. The task was tested under Google Chrome.
### Prerequisites
- Psychopy (v2020.2.8)
- Python (3.7.4)
- Google Chrome (90.0.4430.212) with Javascript (1.7)
### How to use?
This task can be administered entirely online through Pavlovia and/or offline with PsychoPy.

#### Online
- Create a [Pavlovia](https://gitlab.pavlovia.org/users/sign_in) account
- [Fork](https://pavlovia.org/docs/experiments/create-fork) the [Beads Distractor](https://gitlab.pavlovia.org/katielavigne/beads-distractor) task to your account
- In your [Pavlovia dashboard](https://pavlovia.org/dashboard?tab=0), the task should soon be listed under Experiments, which you can click on to View Code, Pilot, or Run. 
#### Offline
- Install [Psychopy](https://www.psychopy.org/download.html)
- Install [Python](https://www.python.org/downloads/)
- Download [Beads Distractor](https://gitlab.pavlovia.org/katielavigne/beads-distractor)
- Extract the archive
- Run Psychopy
- Go to File>Open... locate the folder of the Beads Distractor task and open BEADS.psyexp

#### Offline/Online Capabilities
- After following all steps above, login with your Pavlovia credentials on PsychoPy
- Open the downloaded BEADS.psyexp
- Sync this task with the web project by clicking the left-most globe icon
- Start the experiment with the play button 
- This should launch the experiment in your browser on the pavlovia website
- If you have a warning on the pavlovia website, click on the link and put the experiment in Piloting mode
## Features
- Distractor trials and bead colour randomization are implemented for repeated administrations
- First trial is equivalent to the traditional beads task
- Prevent special characters in the participant's name
- Language selection (French or English) at the beginning of the experiment
- Selection buttons that make it possible to use the task on a tablet or smartphone (drag and drop not available for confidence ratings - click only)
- Preview of the score when drag & drop is performed on web browser
- Automatically computing scores once the participant has finished the trials
- The computed scores are sent directly to the database of the Redcap online survey manager
## Code Reference
N/A
## Code Example
The code interacts with the Builder components.


For example, if we create a Text component called "myText" with the builder and write "MAGIC DOES NOT EXIST" in its Text field. 
Then we can create a Code component that will contain the following Javascript code:

myText.text = "ABRACADABRA";

If we run the experiment online, myText will display ABRACADABRA.
## Outputs

At the end of the task a logfile is created. This file contains the data collected during the task.

We computed scores once the participant finished the trials (scores are computed when they reach the thx screen). These scores are sent directly to the database of the Redcap online survey manager. Below are the different variables that we compute:

| Variables | Description  |
|---|---|
| subject  | Participant's identifier |
| language | Language selected |
| session | Number of the session (session 1 = pre, session 2 = post) |
| date | Date the task was completed |
| task_version | The release version of the task used |
| Beads_orig_dtd | Draws to decision: number of beads drawn before decision (traditional task/1st trial) |
| Beads_orig_match | Match (0 = No, 1 = Yes): Does the selected jar match the highest probability jar? (traditional task/1st trial)|
| Beads_orig_trial_duration | Trial duration (traditional task/1st trial)|
| Beads_orig_confidence_rating | Confidence rating between 0 and 1 (0=0; 1=100) on the first trial (traditional task)|
| Beads_targ_dtd | Mean draws to decision on target trials |
| Beads_targ_match |Mean match on target trials|
| Beads_targ_trial_duration | Mean duration of target trials|
| Beads_targ_confidence_rating | Mean confidence rating of target trials between 0 and 1 (0=0; 1=100)|

The exact calculations can be found in the code and are based on the following macros: https://drive.google.com/drive/folders/1UyBh4STZDGWsQuD7OjtX1u7Uq4cQE8qI?usp=sharing

## Contribute
E-mail: <katie.lavigne@mcgill.ca>
## Authors and acknowledgment
This Beads task was designed by Ryan Balzan and Ben McLean. This version was developed by Katie Lavigne and Caroline Dakoure.
## License
Credit this work by copying the following to your credits section:

BEADS Lavigne et al. (https://gitlab.pavlovia.org/katielavigne/beads-distractor)
Licensed under GNU General Public License v3.0.
https://www.gnu.org/licenses/gpl-3.0.txt
## References
<a id="1">[1]</a> McLean, B. F., Mattiske, J. K., and Balzan, R. P, 2018. Towards a reliable repeated-measures beads task for assessing the jumping to conclusions bias. Psychiatry research. 265, 200-207. doi.org/10.1016/j.psychres.2018.04.043.
