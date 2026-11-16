/************************* 
 * Beads-Distractor *
 *************************/


// store info about the experiment session:
let expName = 'beads-distractor';  // from the Builder filename that created this script
let expInfo = {
    'participant': '',
    'session': '001',
};

// Start code blocks for 'Before Experiment'
/* 
Use danfos to convert the data into dataframe
We will be able to make calculations on the data more easily
and in a clearer way for a future reading of the code.
The calculations are also similar to those with Python and Pandas,
so it is less work.
*/

var danfosUrl = './bundle.min.js';


function dynamicallyLoadScript(url) {
    var script = document.createElement("script");  // create a script DOM node
    script.src = url;  // set its src to the provided URL

    document.head.appendChild(script);  // add it to the end of the head section of the page (could change 'head' to 'body' to add it to the end of the body section instead)
}

dynamicallyLoadScript(danfosUrl);
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0,0,0]),
  units: 'height',
  waitBlanking: true,
  backgroundImage: '',
  backgroundFit: 'none',
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); },flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(langRoutineBegin());
flowScheduler.add(langRoutineEachFrame());
flowScheduler.add(langRoutineEnd());
flowScheduler.add(instrRoutineBegin());
flowScheduler.add(instrRoutineEachFrame());
flowScheduler.add(instrRoutineEnd());
const trials_3LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_3LoopBegin(trials_3LoopScheduler));
flowScheduler.add(trials_3LoopScheduler);
flowScheduler.add(trials_3LoopEnd);



flowScheduler.add(instrRoutineBegin());
flowScheduler.add(instrRoutineEachFrame());
flowScheduler.add(instrRoutineEnd());
const trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialsLoopBegin(trialsLoopScheduler));
flowScheduler.add(trialsLoopScheduler);
flowScheduler.add(trialsLoopEnd);



flowScheduler.add(instrRoutineBegin());
flowScheduler.add(instrRoutineEachFrame());
flowScheduler.add(instrRoutineEnd());
const trials_2LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_2LoopBegin(trials_2LoopScheduler));
flowScheduler.add(trials_2LoopScheduler);
flowScheduler.add(trials_2LoopEnd);



flowScheduler.add(thanksRoutineBegin());
flowScheduler.add(thanksRoutineEachFrame());
flowScheduler.add(thanksRoutineEnd());
flowScheduler.add(quitPsychoJS, 'Thank you for your patience.', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, 'Thank you for your patience.', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    // resources:
    {'name': 'beadsTaskConditions_num_en1_trial.csv', 'path': 'beadsTaskConditions_num_en1_trial.csv'},
    {'name': 'stimuli/GB1.png', 'path': 'stimuli/GB1.png'},
    {'name': 'beadsTaskConditions_num_en1.csv', 'path': 'beadsTaskConditions_num_en1.csv'},
    {'name': 'stimuli/BR3.png', 'path': 'stimuli/BR3.png'},
    {'name': 'stimuli/YR3.png', 'path': 'stimuli/YR3.png'},
    {'name': 'stimuli/GB4.png', 'path': 'stimuli/GB4.png'},
    {'name': 'stimuli/RG3.png', 'path': 'stimuli/RG3.png'},
    {'name': 'stimuli/YR4.png', 'path': 'stimuli/YR4.png'},
    {'name': 'stimuli/GB3.png', 'path': 'stimuli/GB3.png'},
    {'name': 'stimuli/RG4.png', 'path': 'stimuli/RG4.png'},
    {'name': 'stimuli/GY3.png', 'path': 'stimuli/GY3.png'},
    {'name': 'stimuli/YB4.png', 'path': 'stimuli/YB4.png'},
    {'name': 'default.png', 'path': 'https://pavlovia.org/assets/default/default.png'},
    {'name': 'button.png', 'path': 'button.png'},
    {'name': 'stimuli/BR1.png', 'path': 'stimuli/BR1.png'},
    {'name': 'stimuli/BR2.png', 'path': 'stimuli/BR2.png'},
    {'name': 'stimuli/BR3.png', 'path': 'stimuli/BR3.png'},
    {'name': 'stimuli/GB1.png', 'path': 'stimuli/GB1.png'},
    {'name': 'stimuli/GB2.png', 'path': 'stimuli/GB2.png'},
    {'name': 'stimuli/GB3.png', 'path': 'stimuli/GB3.png'},
    {'name': 'stimuli/GB4.png', 'path': 'stimuli/GB4.png'},
    {'name': 'stimuli/GY1.png', 'path': 'stimuli/GY1.png'},
    {'name': 'stimuli/GY2.png', 'path': 'stimuli/GY2.png'},
    {'name': 'stimuli/GY3.png', 'path': 'stimuli/GY3.png'},
    {'name': 'stimuli/GY4.png', 'path': 'stimuli/GY4.png'},
    {'name': 'stimuli/RG1.png', 'path': 'stimuli/RG1.png'},
    {'name': 'stimuli/RG2.png', 'path': 'stimuli/RG2.png'},
    {'name': 'stimuli/RG3.png', 'path': 'stimuli/RG3.png'},
    {'name': 'stimuli/RG4.png', 'path': 'stimuli/RG4.png'},
    {'name': 'stimuli/Text.xcf', 'path': 'stimuli/Text.xcf'},
    {'name': 'stimuli/YB1.png', 'path': 'stimuli/YB1.png'},
    {'name': 'stimuli/YB2.png', 'path': 'stimuli/YB2.png'},
    {'name': 'stimuli/YB3.png', 'path': 'stimuli/YB3.png'},
    {'name': 'stimuli/YB4.png', 'path': 'stimuli/YB4.png'},
    {'name': 'stimuli/YR1.png', 'path': 'stimuli/YR1.png'},
    {'name': 'stimuli/YR2.png', 'path': 'stimuli/YR2.png'},
    {'name': 'stimuli/YR3.png', 'path': 'stimuli/YR3.png'},
    {'name': 'stimuli/YR4.png', 'path': 'stimuli/YR4.png'},
    {'name': 'beads.png', 'path': 'beads.png'},
    {'name': 'beadsTaskConditions_num_en.csv', 'path': 'beadsTaskConditions_num_en.csv'},
    {'name': 'bundle.min.js', 'path': 'bundle.min.js'},
    {'name': 'button.png', 'path': 'button.png'},
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);


var currentLoop;
var frameDur;
async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2024.2.4';
  expInfo['OS'] = window.navigator.platform;


  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  

  
  psychoJS.experiment.dataFileName = (("." + "/") + `data/${expInfo["participant"]}_${expName}_${expInfo["date"]}`);
  psychoJS.experiment.field_separator = '\t';


  return Scheduler.Event.NEXT;
}


var langClock;
var date1;
var d;
var startingDate;
var red;
var french;
var english;
var trialConditions;
var redcapVars;
var instrClock;
var thisExp;
var win;
var event;
var beadsImage;
var beads_instr;
var beadsA_instr;
var beadsB_instr;
var instructionstext;
var next_instr;
var txt_next_instr;
var mouse_instr;
var trialClock;
var preventClick;
var col;
var currentTrial;
var score;
var beadsimg1;
var beadstxtA;
var beadstxtB;
var mouse;
var bead1;
var bead2;
var bead3;
var bead4;
var bead5;
var bead6;
var bead7;
var bead8;
var bead9;
var bead10;
var ratingtext;
var jarA;
var jarB;
var jarAtext;
var jarBtext;
var scaletext;
var rating;
var rating_value;
var rect_draw;
var rect_decide;
var text_draw;
var text_decide;
var Score;
var itiClock;
var polygon;
var thanksClock;
var thx;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "lang"
  langClock = new util.Clock();
  // Run 'Begin Experiment' code from code_lang
  
  // Initialize starting date
  date1 = new Date().toLocaleString("en-US", {timeZone: "America/New_York"});
  d = new Date(date1);
  startingDate =  d.getFullYear() + "-" + (d.getMonth()+1) + "-" + d.getDate() + " " +
  d.getHours() + ":" + d.getMinutes();
  
  //Initialize variables to change the color of highlighed rect
  red = new util.Color("red");
  
  //Set french or english variable to true when the language is selected
  french = false;
  english = true;
  
  trialConditions = "beadsTaskConditions_num_en.csv"
  redcapVars = [];
  
  //Remove illegal characters in participants' name to avoid errors in filenames
  function CheckFilename(){
     expInfo['participant']= expInfo['participant'].replace(/([^.a-z0-9]+)/gi, '-');
  }
  
  // Load redcap variables from Google Spreadsheet
  function LoadRedcapVars(redcapVars){
      try {
          // Retrieve data between B2 and max range
          let url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vR2HrrKB78yxkxRABtTlghA1reADPaQN32V5oJ2BbRXEZOhr8YrkGDZaIVZtjqNMXWTLzeG6-xRaEBl/pub?gid=964834201&range=B2:AA2&output=csv";
          var xmlhttp = new XMLHttpRequest();
          xmlhttp.onreadystatechange = function () {
              if (xmlhttp.readyState == 4) {
                  let array = xmlhttp.responseText.split(',');
                  for (let i = 0; i < array.length; i++) {
                      redcapVars.push(array[i]);
                  }
              }
          };
          xmlhttp.open("GET", url, true);
          xmlhttp.send(null);
          return redcapVars;
      }
      catch(err) {
          console.log("Erreur while loading Redcap variables", err.message);
      }
      
  }
  
  CheckFilename();
  redcapVars = LoadRedcapVars(redcapVars);
  // Initialize components for Routine "instr"
  instrClock = new util.Clock();
  // Run 'Begin Experiment' code from code_JS
  thisExp=psychoJS.experiment;
  win=psychoJS.window;
  event=psychoJS.eventManager;
  Array.prototype.append = [].push;
  
  //We will change the pictures accordingly to the selected language
  beadsImage = "beads.png";
  
  //mouseImage = "mouse_instr_en.png";
  beads_instr = new visual.ImageStim({
    win : psychoJS.window,
    name : 'beads_instr', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0, 
    pos : [0, 0.36], 
    draggable: false,
    size : [0.39, 0.25],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : -1.0 
  });
  beadsA_instr = new visual.TextStim({
    win: psychoJS.window,
    name: 'beadsA_instr',
    text: '85% yellow\n15% red',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.112), 0.26], draggable: false, height: 0.018,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color([(- 1), (- 1), (- 1)]),  opacity: 1,
    depth: -2.0 
  });
  
  beadsB_instr = new visual.TextStim({
    win: psychoJS.window,
    name: 'beadsB_instr',
    text: '85% red\n15% yellow',
    font: 'Arial',
    units: undefined, 
    pos: [0.105, 0.26], draggable: false, height: 0.018,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color([(- 1), (- 1), (- 1)]),  opacity: 1,
    depth: -3.0 
  });
  
  instructionstext = new visual.TextStim({
    win: psychoJS.window,
    name: 'instructionstext',
    text: 'In this task, you will be shown two jars full of 100 colored beads similar to those above. One jar will contain 85% beads in one color (in this case yellow), and 15% beads in another color (in this case red). The other jar will contain colored beads in the opposite ratio.\nFor each trial, one of the jars will be randomly selected, but you will not be told which one. The computer will randomly draw beads from the selected jar. Your job is to decide which jar the beads are being drawn from. Click the left mouse button to draw another bead and the right mouse button to make a decision.\nYou can continue requesting up to a certain number of beads until you feel confident about making a decision. Jars will not swap mid-game.\nClick on next to begin.\n',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.085)], draggable: false, height: 0.029,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color([1, 1, 1]),  opacity: 1,
    depth: -4.0 
  });
  
  next_instr = new visual.ImageStim({
    win : psychoJS.window,
    name : 'next_instr', units : undefined, 
    image : 'button.png', mask : undefined,
    anchor : 'center',
    ori : 0, 
    pos : [0, (- 0.454)], 
    draggable: false,
    size : [0.25, 0.05],
    color : new util.Color([1, 1, 1]), opacity : 0.73,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : -5.0 
  });
  txt_next_instr = new visual.TextStim({
    win: psychoJS.window,
    name: 'txt_next_instr',
    text: 'NEXT',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.023,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color([(- 1), (- 1), (- 1)]),  opacity: 0.73,
    depth: -6.0 
  });
  
  mouse_instr = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_instr.mouseClock = new util.Clock();
  // Initialize components for Routine "trial"
  trialClock = new util.Clock();
  // Run 'Begin Experiment' code from code
  preventClick = function (event) { event.preventDefault(); }
  document.addEventListener("contextmenu", preventClick, event, false);
  col = new util.Color('black');
  currentTrial = 1;
  score = 0;
  
  //Decision jar that will be equal to the jar chosen by the participant
  
  beadsimg1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'beadsimg1', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0, 
    pos : [0, 0.275], 
    draggable: false,
    size : [0.49, 0.27],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : -1.0 
  });
  beadstxtA = new visual.TextStim({
    win: psychoJS.window,
    name: 'beadstxtA',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.137), 0.115], draggable: false, height: 0.02,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: 1,
    depth: -2.0 
  });
  
  beadstxtB = new visual.TextStim({
    win: psychoJS.window,
    name: 'beadstxtB',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0.135, 0.115], draggable: false, height: 0.02,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color([(- 1), (- 1), (- 1)]),  opacity: 1,
    depth: -3.0 
  });
  
  mouse = new core.Mouse({
    win: psychoJS.window,
  });
  mouse.mouseClock = new util.Clock();
  bead1 = new visual.Polygon({
    win: psychoJS.window, name: 'bead1', 
    edges: 100, size:[0.1, 0.1],
    ori: 0, 
    pos: [(- 0.675), 0], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 0, 
    lineColor: undefined, 
    fillColor: new util.Color('white'), 
    colorSpace: 'rgb', 
    opacity: 1, 
    depth: -5, 
    interpolate: false, 
  });
  
  bead2 = new visual.Polygon({
    win: psychoJS.window, name: 'bead2', 
    edges: 100, size:[0.1, 0.1],
    ori: 0, 
    pos: [(- 0.525), 0], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 0, 
    lineColor: undefined, 
    fillColor: new util.Color('white'), 
    colorSpace: 'rgb', 
    opacity: 1, 
    depth: -6, 
    interpolate: false, 
  });
  
  bead3 = new visual.Polygon({
    win: psychoJS.window, name: 'bead3', 
    edges: 100, size:[0.1, 0.1],
    ori: 0, 
    pos: [(- 0.375), 0], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 0, 
    lineColor: undefined, 
    fillColor: new util.Color('white'), 
    colorSpace: 'rgb', 
    opacity: 1, 
    depth: -7, 
    interpolate: false, 
  });
  
  bead4 = new visual.Polygon({
    win: psychoJS.window, name: 'bead4', 
    edges: 100, size:[0.1, 0.1],
    ori: 0, 
    pos: [(- 0.225), 0], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 0, 
    lineColor: undefined, 
    fillColor: new util.Color('white'), 
    colorSpace: 'rgb', 
    opacity: 1, 
    depth: -8, 
    interpolate: false, 
  });
  
  bead5 = new visual.Polygon({
    win: psychoJS.window, name: 'bead5', 
    edges: 100, size:[0.1, 0.1],
    ori: 0, 
    pos: [(- 0.075), 0], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 0, 
    lineColor: undefined, 
    fillColor: new util.Color('white'), 
    colorSpace: 'rgb', 
    opacity: 1, 
    depth: -9, 
    interpolate: false, 
  });
  
  bead6 = new visual.Polygon({
    win: psychoJS.window, name: 'bead6', 
    edges: 100, size:[0.1, 0.1],
    ori: 0, 
    pos: [0.0, 0], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 0, 
    lineColor: undefined, 
    fillColor: new util.Color('white'), 
    colorSpace: 'rgb', 
    opacity: 1, 
    depth: -10, 
    interpolate: false, 
  });
  
  bead7 = new visual.Polygon({
    win: psychoJS.window, name: 'bead7', 
    edges: 100, size:[0.1, 0.1],
    ori: 0, 
    pos: [0.225, 0], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 0, 
    lineColor: undefined, 
    fillColor: new util.Color('white'), 
    colorSpace: 'rgb', 
    opacity: 1, 
    depth: -11, 
    interpolate: false, 
  });
  
  bead8 = new visual.Polygon({
    win: psychoJS.window, name: 'bead8', 
    edges: 100, size:[0.1, 0.1],
    ori: 0, 
    pos: [0.375, 0], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 0, 
    lineColor: undefined, 
    fillColor: new util.Color('white'), 
    colorSpace: 'rgb', 
    opacity: 1, 
    depth: -12, 
    interpolate: false, 
  });
  
  bead9 = new visual.Polygon({
    win: psychoJS.window, name: 'bead9', 
    edges: 100, size:[0.1, 0.1],
    ori: 0, 
    pos: [0.525, 0], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 0, 
    lineColor: undefined, 
    fillColor: new util.Color('white'), 
    colorSpace: 'rgb', 
    opacity: 1, 
    depth: -13, 
    interpolate: false, 
  });
  
  bead10 = new visual.Polygon({
    win: psychoJS.window, name: 'bead10', 
    edges: 100, size:[0.1, 0.1],
    ori: 0, 
    pos: [0.675, 0], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 0, 
    lineColor: undefined, 
    fillColor: new util.Color('white'), 
    colorSpace: 'rgb', 
    opacity: 1, 
    depth: -14, 
    interpolate: false, 
  });
  
  ratingtext = new visual.TextStim({
    win: psychoJS.window,
    name: 'ratingtext',
    text: 'From which jar were the beads drawn?',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.1)], draggable: false, height: 0.03,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -15.0 
  });
  
  jarA = new visual.ImageStim({
    win : psychoJS.window,
    name : 'jarA', units : undefined, 
    image : 'button.png', mask : undefined,
    anchor : 'center',
    ori : 0, 
    pos : [(- 0.15), (- 0.17)], 
    draggable: false,
    size : [0.17, 0.05],
    color : new util.Color([1, 1, 1]), opacity : 0.73,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : -16.0 
  });
  jarB = new visual.ImageStim({
    win : psychoJS.window,
    name : 'jarB', units : undefined, 
    image : 'button.png', mask : undefined,
    anchor : 'center',
    ori : 0, 
    pos : [0.15, (- 0.17)], 
    draggable: false,
    size : [0.15, 0.05],
    color : new util.Color([1, 1, 1]), opacity : 0.73,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : -17.0 
  });
  jarAtext = new visual.TextStim({
    win: psychoJS.window,
    name: 'jarAtext',
    text: 'JAR A',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.03,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color([(- 1), (- 1), (- 1)]),  opacity: 0.73,
    depth: -18.0 
  });
  
  jarBtext = new visual.TextStim({
    win: psychoJS.window,
    name: 'jarBtext',
    text: 'JAR B',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.03,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 0.73,
    depth: -19.0 
  });
  
  scaletext = new visual.TextStim({
    win: psychoJS.window,
    name: 'scaletext',
    text: 'Please indicate your degree of confidence:',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.28)], draggable: false, height: 0.03,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -20.0 
  });
  
  rating = new visual.Slider({
    win: psychoJS.window, name: 'rating',
    startValue: undefined,
    size: [1, 0.1], pos: [0, (- 0.35)], ori: 0, units: psychoJS.window.units,
    labels: ["0", "100"], fontSize: 0.05, ticks: [0, 100],
    granularity: 0, style: ["RATING"],
    color: new util.Color('LightGray'), markerColor: new util.Color('black'), lineColor: new util.Color('White'), 
    opacity: 1, fontFamily: 'Arial', bold: true, italic: false, depth: -21, 
    flip: false,
  });
  
  rating_value = new visual.TextStim({
    win: psychoJS.window,
    name: 'rating_value',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.425)], draggable: false, height: 0.035,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -22.0 
  });
  
  rect_draw = new visual.ImageStim({
    win : psychoJS.window,
    name : 'rect_draw', units : undefined, 
    image : 'button.png', mask : undefined,
    anchor : 'center',
    ori : 0, 
    pos : [0, (- 0.17)], 
    draggable: false,
    size : [0.35, 0.07],
    color : new util.Color([1, 1, 1]), opacity : 0.73,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : -23.0 
  });
  rect_decide = new visual.ImageStim({
    win : psychoJS.window,
    name : 'rect_decide', units : undefined, 
    image : 'button.png', mask : undefined,
    anchor : 'center',
    ori : 0, 
    pos : [0, (- 0.28)], 
    draggable: false,
    size : [0.35, 0.07],
    color : new util.Color([1, 1, 1]), opacity : 0.73,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : -24.0 
  });
  text_draw = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_draw',
    text: 'DRAW',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.025,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color([(- 1), (- 1), (- 1)]),  opacity: 0.73,
    depth: -25.0 
  });
  
  text_decide = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_decide',
    text: 'DECIDE',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.025,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color([(- 1), (- 1), (- 1)]),  opacity: 0.73,
    depth: -26.0 
  });
  
  Score = new visual.TextStim({
    win: psychoJS.window,
    name: 'Score',
    text: '',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0], draggable: false, height: 0.1,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('green'),  opacity: 1,
    depth: -27.0 
  });
  
  // Initialize components for Routine "iti"
  itiClock = new util.Clock();
  polygon = new visual.ShapeStim ({
    win: psychoJS.window, name: 'polygon', 
    vertices: 'cross', size:[0.1, 0.1],
    ori: 0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 0, 
    lineColor: undefined, 
    fillColor: new util.Color('white'), 
    colorSpace: 'rgb', 
    opacity: 1, 
    depth: -1, 
    interpolate: false, 
  });
  
  // Initialize components for Routine "thanks"
  thanksClock = new util.Clock();
  thx = new visual.TextStim({
    win: psychoJS.window,
    name: 'thx',
    text: 'Thank you for participating!',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.1,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var langMaxDurationReached;
var count;
var langMaxDuration;
var langComponents;
function langRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'lang' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    langClock.reset();
    routineTimer.reset();
    langMaxDurationReached = false;
    // update component parameters for each repeat
    thisExp=psychoJS.experiment;
    win=psychoJS.window;
    event=psychoJS.eventManager;
    Array.prototype.append = [].push;
    count = 0;
    psychoJS.experiment.addData('lang.started', globalClock.getTime());
    langMaxDuration = null
    // keep track of which components have finished
    langComponents = [];
    
    langComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function langRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'lang' ---
    // get current time
    t = langClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // Run 'Each Frame' code from code_lang
    //Change the color of highlighed rect
    function HighlightRect(rec1, rec2, txt_rec1, txt_rec2, mouse) {
         if (rec1.contains(mouse)) {
            rec1.setOpacity(0.99);
            txt_rec1.setOpacity(2);
         } 
        else{
            rec1.setOpacity(0.73);
            txt_rec1.setOpacity(0.73);
        }
         if (rec2.contains(mouse)) {
            rec2.setOpacity(0.99);
            txt_rec2.setOpacity(2);
         } 
        else{
            rec2.setOpacity(0.73);
            txt_rec2.setOpacity(0.73);
        }
    }
    
    //Function that is going to set the chosen language
    //function SelectLanguage(rec1, rec2, mouse){
    //    if (rec1.contains(mouse) && mouse.getPressed()[0] === 1 ) {
    //        french = true;
    //        trialConditions = "beadsTaskConditions_num_fr.csv";
    //    }
    //    else if (rec2.contains(mouse) && mouse.getPressed()[0] === 1 ) {
    //        english = true;
    //        trialConditions = "beadsTaskConditions_num_en.csv";
    //    }
    //}
    
    //HighlightRect(rect1,  rect2, txt_rect1, txt_rect2, mouse1);
    //SelectLanguage(rect1,  rect2, mouse1);
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    langComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function langRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'lang' ---
    langComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('lang.stopped', globalClock.getTime());
    // Run 'End Routine' code from code_lang
    thisExp.addData("Language", english===true ? "en" : "fr");
    // the Routine "lang" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var instrMaxDurationReached;
var gotValidClick;
var instrMaxDuration;
var instrComponents;
function instrRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'instr' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    instrClock.reset();
    routineTimer.reset();
    instrMaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from code_JS
    //Change the text according to the selected language, function SetTxtInstr()
    function SetTxtInstr(){
        
        if (count == 0){
            instructionstext.text = "\nPractice Time!\nIn this experiment, you will see two jars, each with 100 colored beads.\n- Jar 1: 85% beads of one color (e.g., yellow), 15% of another color (e.g., red).\n- Jar 2: The colors are reversed — 85% of the second color, 15% of the first.\nOne jar will be randomly selected, but you won't know which.\n1. Draw a bead by clicking 'DRAW ANOTHER BEAD'.\n2. You can draw up to 10 beads before deciding.\n3. After each bead, you will be asked your confidence level — how confident are you in choosing the jar based on the beads you've drawn so far?\n4. Click 'MAKE A DECISION' to guess which jar the beads came from.\n5. After 10 beads or your decision, the trial will automatically move on.\nYour goal is to identify the jar by drawing beads, making a decision, and providing your confidence level. Good luck!"
            beadsA_instr.text = "\n\n85% yellow \n15% red";
            beadsB_instr.text = "\n\n85% red \n15% yellow";
            //mouseImage = "mouse_instr_en.png";
            txt_next_instr.text = "NEXT";
    
        }
        else if (count == 1)
        {
            instructionstext.text = "\nTime to get serious now!\nIn this experiment, you will see two jars, each with 100 colored beads.\n- Jar 1: 85% beads of one color (e.g., yellow), 15% of another color (e.g., red).\n- Jar 2: The colors are reversed — 85% of the second color, 15% of the first.\nOne jar will be randomly selected, but you won't know which.\n1. Draw a bead by clicking 'DRAW ANOTHER BEAD'.\n2. You can draw up to 10 beads before deciding.\n3. After each bead, you will be asked your confidence level — how confident are you in choosing the jar based on the beads you've drawn so far?\n4. Click 'MAKE A DECISION' to guess which jar the beads came from.\n5. After 10 beads or your decision, the trial will automatically move on.\nYour goal is to identify the jar by drawing beads, making a decision, and providing your confidence level. Good luck!"
            beadsA_instr.text = "\n\n85% yellow \n15% red";
            beadsB_instr.text = "\n\n85% red \n15% yellow";
            //mouseImage = "mouse_instr_fr.png";
            txt_next_instr.text = "NEXT";
        }
        
        else if (count == 2)
        {
            instructionstext.text = "Alert: The jar ratios have changed! The proportion of beads in each jar has now shifted to 60% of one color and 40% of the other. However, all other conditions remain the same, including the scoring system. Keep going and maximize your score! Click on next to begin."
            beadsA_instr.text = "\n\n60% yellow \n40% red";
            beadsB_instr.text = "\n\n60% red \n40% yellow";
            //mouseImage = "mouse_instr_fr.png";
            txt_next_instr.text = "NEXT";
        }
    }
    
    SetTxtInstr();
    //hasResources = false;
    
    /* 
    TODO: load the resources here since the element in the builder is not working properly
    psychoJS._serverManager.prepareResources([
    { name: (itemFile), path: (itemFile) }
    ]);
    if (psychoJS.serverManager.getResourceStatus(core.ServerManager.ALL_RESOURCES) === core.ServerManager.ResourceStatus.DOWNLOADED
    */
    
    /*
    psychoJS._serverManager.prepareResources([
    { name: (itemFile), path: (itemFile) }
    ]);
    */
    beads_instr.setImage(beadsImage);
    txt_next_instr.setPos(next_instr.pos);
    // setup some python lists for storing info about the mouse_instr
    // current position of the mouse:
    mouse_instr.x = [];
    mouse_instr.y = [];
    mouse_instr.leftButton = [];
    mouse_instr.midButton = [];
    mouse_instr.rightButton = [];
    mouse_instr.time = [];
    mouse_instr.clicked_name = [];
    gotValidClick = false; // until a click is received
    mouse_instr.mouseClock.reset();
    psychoJS.experiment.addData('instr.started', globalClock.getTime());
    instrMaxDuration = null
    // keep track of which components have finished
    instrComponents = [];
    instrComponents.push(beads_instr);
    instrComponents.push(beadsA_instr);
    instrComponents.push(beadsB_instr);
    instrComponents.push(instructionstext);
    instrComponents.push(next_instr);
    instrComponents.push(txt_next_instr);
    instrComponents.push(mouse_instr);
    
    instrComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


var prevButtonState;
var _mouseButtons;
var _mouseXYs;
function instrRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'instr' ---
    // get current time
    t = instrClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // Run 'Each Frame' code from code_JS
    //Change the color of highlighed rect
    function HighlightRect(rec1, txt_rec1, mouse) {
         if (rec1.contains(mouse)) {
            rec1.setOpacity(0.99);
            txt_rec1.setOpacity(2);
         } 
        else{
            rec1.setOpacity(0.73);
            txt_rec1.setOpacity(0.73);
        }
    }
    
    HighlightRect(next_instr, txt_next_instr, mouse_instr);
    
    /*
    if (resources.status == FINISHED){
        hasResources = true;
    }
    */
    
    // *beads_instr* updates
    if (t >= 0.0 && beads_instr.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      beads_instr.tStart = t;  // (not accounting for frame time here)
      beads_instr.frameNStart = frameN;  // exact frame index
      
      beads_instr.setAutoDraw(true);
    }
    
    
    // *beadsA_instr* updates
    if (t >= 0.0 && beadsA_instr.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      beadsA_instr.tStart = t;  // (not accounting for frame time here)
      beadsA_instr.frameNStart = frameN;  // exact frame index
      
      beadsA_instr.setAutoDraw(true);
    }
    
    
    // *beadsB_instr* updates
    if (t >= 0.0 && beadsB_instr.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      beadsB_instr.tStart = t;  // (not accounting for frame time here)
      beadsB_instr.frameNStart = frameN;  // exact frame index
      
      beadsB_instr.setAutoDraw(true);
    }
    
    
    // *instructionstext* updates
    if (t >= 0.0 && instructionstext.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instructionstext.tStart = t;  // (not accounting for frame time here)
      instructionstext.frameNStart = frameN;  // exact frame index
      
      instructionstext.setAutoDraw(true);
    }
    
    
    // *next_instr* updates
    if (t >= 0 && next_instr.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      next_instr.tStart = t;  // (not accounting for frame time here)
      next_instr.frameNStart = frameN;  // exact frame index
      
      next_instr.setAutoDraw(true);
    }
    
    
    // *txt_next_instr* updates
    if (t >= 0.0 && txt_next_instr.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      txt_next_instr.tStart = t;  // (not accounting for frame time here)
      txt_next_instr.frameNStart = frameN;  // exact frame index
      
      txt_next_instr.setAutoDraw(true);
    }
    
    // *mouse_instr* updates
    if (t >= 0.0 && mouse_instr.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse_instr.tStart = t;  // (not accounting for frame time here)
      mouse_instr.frameNStart = frameN;  // exact frame index
      
      mouse_instr.status = PsychoJS.Status.STARTED;
      prevButtonState = mouse_instr.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mouse_instr.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse_instr.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          mouse_instr.clickableObjects = eval(next_instr)
          ;// make sure the mouse's clickable objects are an array
          if (!Array.isArray(mouse_instr.clickableObjects)) {
              mouse_instr.clickableObjects = [mouse_instr.clickableObjects];
          }
          // iterate through clickable objects and check each
          for (const obj of mouse_instr.clickableObjects) {
              if (obj.contains(mouse_instr)) {
                  gotValidClick = true;
                  mouse_instr.clicked_name.push(obj.name);
              }
          }
          if (!gotValidClick) {
              mouse_instr.clicked_name.push(null);
          }
          _mouseXYs = mouse_instr.getPos();
          mouse_instr.x.push(_mouseXYs[0]);
          mouse_instr.y.push(_mouseXYs[1]);
          mouse_instr.leftButton.push(_mouseButtons[0]);
          mouse_instr.midButton.push(_mouseButtons[1]);
          mouse_instr.rightButton.push(_mouseButtons[2]);
          mouse_instr.time.push(mouse_instr.mouseClock.getTime());
          if (gotValidClick === true) { // end routine on response
            continueRoutine = false;
          }
        }
      }
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    instrComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instrRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'instr' ---
    instrComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('instr.stopped', globalClock.getTime());
    count = count + 1;
    // store data for psychoJS.experiment (ExperimentHandler)
    psychoJS.experiment.addData('mouse_instr.x', mouse_instr.x);
    psychoJS.experiment.addData('mouse_instr.y', mouse_instr.y);
    psychoJS.experiment.addData('mouse_instr.leftButton', mouse_instr.leftButton);
    psychoJS.experiment.addData('mouse_instr.midButton', mouse_instr.midButton);
    psychoJS.experiment.addData('mouse_instr.rightButton', mouse_instr.rightButton);
    psychoJS.experiment.addData('mouse_instr.time', mouse_instr.time);
    psychoJS.experiment.addData('mouse_instr.clicked_name', mouse_instr.clicked_name);
    
    // the Routine "instr" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var trials_3;
function trials_3LoopBegin(trials_3LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials_3 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 2, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'beadsTaskConditions_num_en1_trial.csv',
      seed: undefined, name: 'trials_3'
    });
    psychoJS.experiment.addLoop(trials_3); // add the loop to the experiment
    currentLoop = trials_3;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    trials_3.forEach(function() {
      snapshot = trials_3.getSnapshot();
    
      trials_3LoopScheduler.add(importConditions(snapshot));
      trials_3LoopScheduler.add(trialRoutineBegin(snapshot));
      trials_3LoopScheduler.add(trialRoutineEachFrame());
      trials_3LoopScheduler.add(trialRoutineEnd(snapshot));
      trials_3LoopScheduler.add(itiRoutineBegin(snapshot));
      trials_3LoopScheduler.add(itiRoutineEachFrame());
      trials_3LoopScheduler.add(itiRoutineEnd(snapshot));
      trials_3LoopScheduler.add(trials_3LoopEndIteration(trials_3LoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function trials_3LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials_3);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trials_3LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var trials;
function trialsLoopBegin(trialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: trialConditions,
      seed: undefined, name: 'trials'
    });
    psychoJS.experiment.addLoop(trials); // add the loop to the experiment
    currentLoop = trials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    trials.forEach(function() {
      snapshot = trials.getSnapshot();
    
      trialsLoopScheduler.add(importConditions(snapshot));
      trialsLoopScheduler.add(trialRoutineBegin(snapshot));
      trialsLoopScheduler.add(trialRoutineEachFrame());
      trialsLoopScheduler.add(trialRoutineEnd(snapshot));
      trialsLoopScheduler.add(itiRoutineBegin(snapshot));
      trialsLoopScheduler.add(itiRoutineEachFrame());
      trialsLoopScheduler.add(itiRoutineEnd(snapshot));
      trialsLoopScheduler.add(trialsLoopEndIteration(trialsLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function trialsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trialsLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var trials_2;
function trials_2LoopBegin(trials_2LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials_2 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'beadsTaskConditions_num_en1.csv',
      seed: undefined, name: 'trials_2'
    });
    psychoJS.experiment.addLoop(trials_2); // add the loop to the experiment
    currentLoop = trials_2;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    trials_2.forEach(function() {
      snapshot = trials_2.getSnapshot();
    
      trials_2LoopScheduler.add(importConditions(snapshot));
      trials_2LoopScheduler.add(trialRoutineBegin(snapshot));
      trials_2LoopScheduler.add(trialRoutineEachFrame());
      trials_2LoopScheduler.add(trialRoutineEnd(snapshot));
      trials_2LoopScheduler.add(itiRoutineBegin(snapshot));
      trials_2LoopScheduler.add(itiRoutineEachFrame());
      trials_2LoopScheduler.add(itiRoutineEnd(snapshot));
      trials_2LoopScheduler.add(trials_2LoopEndIteration(trials_2LoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function trials_2LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials_2);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trials_2LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var trialMaxDurationReached;
var mouse_clicked;
var select_decide;
var jarpic;
var ratingClick;
var ratingstart;
var ratingstart1;
var ratingdone;
var beadnum;
var beads;
var beadcolours;
var true_jar;
var rating_is_initialized;
var confidenceRatings;
var decision_jar;
var colorA_1;
var colorA_2;
var colorB_1;
var colorB_2;
var markerSize;
var finalColor;
var jiggleColors;
var jiggleActive;
var jiggleIndex;
var jiggleFrames;
var jiggleDuration;
var trialMaxDuration;
var trialComponents;
function trialRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'trial' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    trialClock.reset();
    routineTimer.reset();
    trialMaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from code
    //declare variables
    mouse_clicked = false;
    select_decide = false;
    jarpic = jarPicture;
    ratingClick = 0;
    ratingstart = true;
    ratingstart1 = false;
    ratingdone = false;
    beadnum = 0;
    beads = [bead1, bead2, bead3, bead4, bead5, bead6, bead7, bead8, bead9, bead10];
    beadcolours = [];
    true_jar = "jarA";
    rating_is_initialized = false;
    confidenceRatings = [];
    decision_jar = "";
    
    //Jars texts
    colorA_1 = txt_1;
    colorA_2 = txt_2;
    colorB_1 = txt_3;
    colorB_2 = txt_4;
    
    //define slider marker and colour
    rating = new visual.Slider({"win": win, "name": "rating", "size": [1.0, 0.05], "pos": [0, (- 0.35)], "labels": ["0", "100"], "ticks": [0, 100], "granularity": 0, "style": ["rating"], "color": [0.65, 0.65, 0.65], "markerColor": [-1, -1, -1], "font": "Arial", "flip": false, "labelHeight": 0.1});
    rating.size[1] = rating.size[1] / 2;
    markerSize = util.to_px(rating.size, 'height', psychoJS.window)[1];
    
    //randomize beads and colours
    if ((Math.random() > 0.5)) {
        true_jar = "jarB";
        [A_R, A_G, A_B, B_R, B_G, B_B] = [B_R, B_G, B_B, A_R, A_G, A_B];
    }
    for (var i = 0, _pj_a = beads.length; (i < _pj_a); i += 1) {
        if ((colorSequence[i] === "A")) {
            beadcolours.append([A_R,A_G,A_B]);
        } else {
            if ((colorSequence[i] === "B")) {
                beadcolours.append([B_R,B_G,B_B]);
            }
        }
    }
    
    finalColor = [A_R,A_G,A_B]
    jiggleColors = [
      [A_R,A_G,A_B],
      [B_R,B_G,B_B],
    ];
    
    jiggleActive = false;
    jiggleIndex = 0;
    jiggleFrames = 0;
    jiggleDuration = 90;  // 2 seconds at 60 FPS
    
    //Change the text according to the selected language
    function SetTxtTrial(){
        if (english){
            ratingtext.text = "From which jar were the beads drawn?";
            jarAtext.text = "JAR A";
            jarBtext.text = "JAR B";
            scaletext.text = "Please indicate your degree of confidence:";
            text_draw.text = "DRAW ANOTHER BEAD";
            text_decide.text = "MAKE A DECISION";
        }
        else{
            ratingtext.text = "De quel pot viennent les billes?";
            jarAtext.text = "POT A";
            jarBtext.text = "POT B";
            scaletext.text = "S’il vous plaît, veuillez évaluer votre degré de confiance :";
            text_draw.text = "PIGER UNE AUTRE BILLE";
            text_decide.text = "FAIRE VOTRE CHOIX";
        }
    }
    SetTxtTrial();
    beadsimg1.setImage(jarpic);
    // setup some python lists for storing info about the mouse
    // current position of the mouse:
    mouse.x = [];
    mouse.y = [];
    mouse.leftButton = [];
    mouse.midButton = [];
    mouse.rightButton = [];
    mouse.time = [];
    mouse.clicked_name = [];
    gotValidClick = false; // until a click is received
    mouse.mouseClock.reset();
    bead1.setFillColor(new util.Color([0, 0, 0]));
    bead2.setFillColor(new util.Color([0, 0, 0]));
    bead3.setFillColor(new util.Color([0, 0, 0]));
    bead4.setFillColor(new util.Color([0, 0, 0]));
    bead5.setFillColor(new util.Color([0, 0, 0]));
    bead6.setFillColor(new util.Color([0, 0, 0]));
    bead7.setFillColor(new util.Color([0, 0, 0]));
    bead8.setFillColor(new util.Color([0, 0, 0]));
    bead9.setFillColor(new util.Color([0, 0, 0]));
    bead10.setFillColor(new util.Color([0, 0, 0]));
    jarAtext.setPos(jarA.pos);
    jarBtext.setColor(new util.Color([(- 1), (- 1), (- 1)]));
    jarBtext.setPos(jarB.pos);
    rating.reset()
    rating_value.setText('');
    text_draw.setPos(rect_draw.pos);
    text_decide.setPos(rect_decide.pos);
    Score.setPos([0.7, 0.8]);
    Score.setText('bye\n');
    psychoJS.experiment.addData('trial.started', globalClock.getTime());
    trialMaxDuration = null
    // keep track of which components have finished
    trialComponents = [];
    trialComponents.push(beadsimg1);
    trialComponents.push(beadstxtA);
    trialComponents.push(beadstxtB);
    trialComponents.push(mouse);
    trialComponents.push(bead1);
    trialComponents.push(bead2);
    trialComponents.push(bead3);
    trialComponents.push(bead4);
    trialComponents.push(bead5);
    trialComponents.push(bead6);
    trialComponents.push(bead7);
    trialComponents.push(bead8);
    trialComponents.push(bead9);
    trialComponents.push(bead10);
    trialComponents.push(ratingtext);
    trialComponents.push(jarA);
    trialComponents.push(jarB);
    trialComponents.push(jarAtext);
    trialComponents.push(jarBtext);
    trialComponents.push(scaletext);
    trialComponents.push(rating);
    trialComponents.push(rating_value);
    trialComponents.push(rect_draw);
    trialComponents.push(rect_decide);
    trialComponents.push(text_draw);
    trialComponents.push(text_decide);
    trialComponents.push(Score);
    
    trialComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function trialRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'trial' ---
    // get current time
    t = trialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // Run 'Each Frame' code from code
    // first bead appears right away
    if(beadnum == 0)
    {
        beads[5].setFillColor(new util.Color(beadcolours[1]));
        beadnum += 1;
    }
    
    // modify slider marker and colour
    if (!rating_is_initialized && rating.status === STARTED){
        try {
            rating._skin.STANDARD.MARKER_COLOR = col;
            rating._skin.MARKER_SIZE = [0.05, 0.05];
            rating._onChange(true)();
            //rating._setupSlider();
        }
        catch (err) {}
        rating_is_initialized  = true;
    }
    
    // display rating value
    if (rating.markerPos !== 0 && rating.markerPos !== undefined) {
        rating_value.text = Math.round(rating.markerPos);
    }
    
    // show jar selection
    if (select_decide === true && ratingdone === false && (mouse.getPressed()[0] === 1 && jarA.contains(mouse))) {
        decision_jar = "jarA";
        ratingstart = true;
    }
    if (select_decide === true && ratingdone === false && (mouse.getPressed()[0] === 1 && jarB.contains(mouse))) {
        decision_jar = "jarB";
        ratingstart = true;
    }
    
    // As soon as the rating of the confidence is done, the participants can no longer change the selected jar
    if (rating.getRating() !== undefined){
        if(decision_jar !== "")
        {
            ratingdone = true;
         }
    //    else
    //    {
    //        ratingstart = false;
    //        thisExp.addData("rating_draw", rating.getRating());
    //        rating.reset();
    //        ratingdone = true;     }
    }
    
    if (ratingstart === true && decision_jar === "" && (rating.getRating() !== undefined) && (trialClock.getTime() > (rating.getRT() + 1)) && rating.getRating() === rating.markerPos) {
        ratingstart = false;
    //    thisExp.addData("rating_draw", rating.getRating());
        confidenceRatings.push(rating.getRating());
        rating.reset();
    //    rating.setOpacity(0.0);
    }
    
    // move to next trial after rating + 1 second (allow for change in ratings within 1 second)
    if (decision_jar !== "" && (rating.getRating() !== undefined) && (trialClock.getTime() > (rating.getRT() + 1)) && rating.getRating() === rating.markerPos) {
        continueRoutine = false;
    }
    
    if (!ratingstart) {
    //    HighlightRect(rect_draw, rect_decide, text_draw, text_decide, mouse);
        rating.reset();
        rating.markerPos = 0;
        rect_draw.setOpacity(1.0);
        text_draw.setOpacity(1.0);
        rect_decide.setOpacity(1.0);
        text_decide.setOpacity(1.0);
        rating.setOpacity(0.0);
        ratingtext.setOpacity(0.0);
        scaletext.setOpacity(0.0);
        rating_value.setOpacity(0.0);
        rating_value.text = "0";
    } else
    {
        rect_draw.setOpacity(0.0);
        text_draw.setOpacity(0.0);
        rect_decide.setOpacity(0.0);
        text_decide.setOpacity(0.0);
    //    rating.setOpacity(1.0);
        ratingtext.setOpacity(1.0);
        scaletext.setOpacity(1.0);
        rating_value.setOpacity(1.0);
    
    }
    
    //Change the color of highlighed rect
    function HighlightRect(rec1, rec2, txt_rec1, txt_rec2, mouse) {
        if(rec1.opacity !== 0.0)
        {
             if (rec1.contains(mouse)) {
                rec1.setOpacity(0.99);
                txt_rec1.setOpacity(2);
             } 
            else{
                rec1.setOpacity(0.73);
                txt_rec1.setOpacity(0.73);
            }
             if (rec2.contains(mouse)) {
                rec2.setOpacity(0.99);
                txt_rec2.setOpacity(2);
             } 
            else{
                rec2.setOpacity(0.73);
                txt_rec2.setOpacity(0.73);
            }
        }
    }
    
    //Change the color of highlighed rect. We won't highligh if participant can not rate anymore 
    function HighlightRect(rec1, rec2, txt_rec1, txt_rec2, mouse, ratingdone) {
        if (!ratingdone && rec1.opacity !== 0){
             if (rec1.contains(mouse)) {
                rec1.setOpacity(0.99);
                txt_rec1.setOpacity(2);
             } 
            else{
                rec1.setOpacity(0.73);
                txt_rec1.setOpacity(0.73);
            }
             if (rec2.contains(mouse)) {
                rec2.setOpacity(0.99);
                txt_rec2.setOpacity(2);
             } 
            else{
                rec2.setOpacity(0.73);
                txt_rec2.setOpacity(0.73);
            }
        }
    }
    
    if(select_decide === true)
    {
        if(decision_jar === "")
        {
                rating.setOpacity(0.0);
                ratingtext.setOpacity(0.0);
        }
        else
        {
                rating.setOpacity(1.0);
                ratingtext.setOpacity(1.0);
        }
    }
    
    //Perform actions depending on clicked button (DRAW/DECIDE)
    function SelectChoice(rec1, rec2, mouse){
        if (select_decide !== true && rec1.contains(mouse) && mouse.getPressed()[0] === 1 && rec1.opacity !== 0) {
             if ((! mouse_clicked)) 
             {
                mouse_clicked = true;
                if ((beadnum === 10))
                {
                    beadnum = 11;
                    continueRoutine = false;
                }
                else if((!jiggleActive) && (beadnum < beads.length))
                {
                    jiggleActive = true;
                    jiggleIndex = 0;
                    jiggleFrames = 0;
                    finalColor = beadcolours[beadnum];  // assumed to be [r, g, b]
    //                beads[beadnum].setFillColor(finalColor, "rgb");
    //                beadnum += 1;
                }
             }
        }
        else {
                mouse_clicked = false;
        }
        
        if (rec2.contains(mouse) && mouse.getPressed()[0] === 1 && jiggleActive == false) {
           select_decide = true;
    //       ratingstart = true;
        }
    }
    
    if(select_decide === true)
    {
       ratingtext.setOpacity(1.0);
    }
    
    if (jiggleActive && (beadnum < beads.length))
    {
         if (jiggleFrames < jiggleDuration) {
            // Make the bead transparent
            beads[5].setOpacity(0.0);
            jiggleFrames += 1;
        } 
        else {
            // Show final color with full opacity
            beads[5].setFillColor(finalColor, "rgb");
            beads[5].setOpacity(1.0);
            jiggleActive = false;
            beadnum += 1;
            ratingstart = true;
            rating.setOpacity(1.0);
            scaletext.setOpacity(1.0);
    //        rating.setOpacity(1.0);
        }
    }
    
    Score.text = "Beads Drawn: " + beadnum;
    HighlightRect(rect_draw, rect_decide, text_draw, text_decide, mouse);
    HighlightRect(jarA, jarB, jarAtext, jarBtext, mouse, ratingdone);
    SelectChoice(rect_draw, rect_decide, mouse);
    
    // *beadsimg1* updates
    if (t >= 0.0 && beadsimg1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      beadsimg1.tStart = t;  // (not accounting for frame time here)
      beadsimg1.frameNStart = frameN;  // exact frame index
      
      beadsimg1.setAutoDraw(true);
    }
    
    
    // *beadstxtA* updates
    if (t >= 0.0 && beadstxtA.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      beadstxtA.tStart = t;  // (not accounting for frame time here)
      beadstxtA.frameNStart = frameN;  // exact frame index
      
      beadstxtA.setAutoDraw(true);
    }
    
    
    // *beadstxtB* updates
    if (t >= 0.0 && beadstxtB.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      beadstxtB.tStart = t;  // (not accounting for frame time here)
      beadstxtB.frameNStart = frameN;  // exact frame index
      
      beadstxtB.setAutoDraw(true);
    }
    
    // *mouse* updates
    if (t >= 0 && mouse.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse.tStart = t;  // (not accounting for frame time here)
      mouse.frameNStart = frameN;  // exact frame index
      
      mouse.status = PsychoJS.Status.STARTED;
      prevButtonState = mouse.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mouse.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          mouse.clickableObjects = eval([jarA, jarB, rect_draw, rect_decide])
          ;// make sure the mouse's clickable objects are an array
          if (!Array.isArray(mouse.clickableObjects)) {
              mouse.clickableObjects = [mouse.clickableObjects];
          }
          // iterate through clickable objects and check each
          for (const obj of mouse.clickableObjects) {
              if (obj.contains(mouse)) {
                  gotValidClick = true;
                  mouse.clicked_name.push(obj.name);
              }
          }
          if (!gotValidClick) {
              mouse.clicked_name.push(null);
          }
          _mouseXYs = mouse.getPos();
          mouse.x.push(_mouseXYs[0]);
          mouse.y.push(_mouseXYs[1]);
          mouse.leftButton.push(_mouseButtons[0]);
          mouse.midButton.push(_mouseButtons[1]);
          mouse.rightButton.push(_mouseButtons[2]);
          mouse.time.push(mouse.mouseClock.getTime());
        }
      }
    }
    
    // *bead1* updates
    if (t >= 0.0 && bead1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      bead1.tStart = t;  // (not accounting for frame time here)
      bead1.frameNStart = frameN;  // exact frame index
      
      bead1.setAutoDraw(true);
    }
    
    
    // *bead2* updates
    if (t >= 0 && bead2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      bead2.tStart = t;  // (not accounting for frame time here)
      bead2.frameNStart = frameN;  // exact frame index
      
      bead2.setAutoDraw(true);
    }
    
    
    // *bead3* updates
    if (t >= 0.0 && bead3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      bead3.tStart = t;  // (not accounting for frame time here)
      bead3.frameNStart = frameN;  // exact frame index
      
      bead3.setAutoDraw(true);
    }
    
    
    // *bead4* updates
    if (t >= 0.0 && bead4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      bead4.tStart = t;  // (not accounting for frame time here)
      bead4.frameNStart = frameN;  // exact frame index
      
      bead4.setAutoDraw(true);
    }
    
    
    // *bead5* updates
    if (t >= 0.0 && bead5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      bead5.tStart = t;  // (not accounting for frame time here)
      bead5.frameNStart = frameN;  // exact frame index
      
      bead5.setAutoDraw(true);
    }
    
    
    // *bead6* updates
    if (t >= 0.0 && bead6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      bead6.tStart = t;  // (not accounting for frame time here)
      bead6.frameNStart = frameN;  // exact frame index
      
      bead6.setAutoDraw(true);
    }
    
    
    // *bead7* updates
    if (t >= 0.0 && bead7.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      bead7.tStart = t;  // (not accounting for frame time here)
      bead7.frameNStart = frameN;  // exact frame index
      
      bead7.setAutoDraw(true);
    }
    
    
    // *bead8* updates
    if (t >= 0.0 && bead8.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      bead8.tStart = t;  // (not accounting for frame time here)
      bead8.frameNStart = frameN;  // exact frame index
      
      bead8.setAutoDraw(true);
    }
    
    
    // *bead9* updates
    if (t >= 0.0 && bead9.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      bead9.tStart = t;  // (not accounting for frame time here)
      bead9.frameNStart = frameN;  // exact frame index
      
      bead9.setAutoDraw(true);
    }
    
    
    // *bead10* updates
    if (t >= 0.0 && bead10.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      bead10.tStart = t;  // (not accounting for frame time here)
      bead10.frameNStart = frameN;  // exact frame index
      
      bead10.setAutoDraw(true);
    }
    
    
    // *ratingtext* updates
    if (((select_decide == 1)) && ratingtext.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ratingtext.tStart = t;  // (not accounting for frame time here)
      ratingtext.frameNStart = frameN;  // exact frame index
      
      ratingtext.setAutoDraw(true);
    }
    
    
    // *jarA* updates
    if (((select_decide == 1)) && jarA.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      jarA.tStart = t;  // (not accounting for frame time here)
      jarA.frameNStart = frameN;  // exact frame index
      
      jarA.setAutoDraw(true);
    }
    
    
    // *jarB* updates
    if (((select_decide == 1)) && jarB.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      jarB.tStart = t;  // (not accounting for frame time here)
      jarB.frameNStart = frameN;  // exact frame index
      
      jarB.setAutoDraw(true);
    }
    
    
    // *jarAtext* updates
    if (((select_decide == 1)) && jarAtext.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      jarAtext.tStart = t;  // (not accounting for frame time here)
      jarAtext.frameNStart = frameN;  // exact frame index
      
      jarAtext.setAutoDraw(true);
    }
    
    
    // *jarBtext* updates
    if (((select_decide == 1)) && jarBtext.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      jarBtext.tStart = t;  // (not accounting for frame time here)
      jarBtext.frameNStart = frameN;  // exact frame index
      
      jarBtext.setAutoDraw(true);
    }
    
    
    // *scaletext* updates
    if (((ratingstart == 1)) && scaletext.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      scaletext.tStart = t;  // (not accounting for frame time here)
      scaletext.frameNStart = frameN;  // exact frame index
      
      scaletext.setAutoDraw(true);
    }
    
    
    // *rating* updates
    if (((ratingstart == 1)) && rating.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rating.tStart = t;  // (not accounting for frame time here)
      rating.frameNStart = frameN;  // exact frame index
      
      rating.setAutoDraw(true);
    }
    
    
    // *rating_value* updates
    if (((ratingstart == 1)) && rating_value.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rating_value.tStart = t;  // (not accounting for frame time here)
      rating_value.frameNStart = frameN;  // exact frame index
      
      rating_value.setAutoDraw(true);
    }
    
    
    // *rect_draw* updates
    if (t >= 0.0 && rect_draw.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rect_draw.tStart = t;  // (not accounting for frame time here)
      rect_draw.frameNStart = frameN;  // exact frame index
      
      rect_draw.setAutoDraw(true);
    }
    
    if (rect_draw.status === PsychoJS.Status.STARTED && Boolean((select_decide == 1))) {
      rect_draw.setAutoDraw(false);
    }
    
    
    // *rect_decide* updates
    if (t >= 0.0 && rect_decide.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rect_decide.tStart = t;  // (not accounting for frame time here)
      rect_decide.frameNStart = frameN;  // exact frame index
      
      rect_decide.setAutoDraw(true);
    }
    
    if (rect_decide.status === PsychoJS.Status.STARTED && Boolean((select_decide == 1))) {
      rect_decide.setAutoDraw(false);
    }
    
    
    // *text_draw* updates
    if (t >= 0.0 && text_draw.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_draw.tStart = t;  // (not accounting for frame time here)
      text_draw.frameNStart = frameN;  // exact frame index
      
      text_draw.setAutoDraw(true);
    }
    
    if (text_draw.status === PsychoJS.Status.STARTED && Boolean((select_decide == 1))) {
      text_draw.setAutoDraw(false);
    }
    
    
    // *text_decide* updates
    if (t >= 0.0 && text_decide.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_decide.tStart = t;  // (not accounting for frame time here)
      text_decide.frameNStart = frameN;  // exact frame index
      
      text_decide.setAutoDraw(true);
    }
    
    if (text_decide.status === PsychoJS.Status.STARTED && Boolean((select_decide == 1))) {
      text_decide.setAutoDraw(false);
    }
    
    
    // *Score* updates
    if (t >= 0 && Score.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Score.tStart = t;  // (not accounting for frame time here)
      Score.frameNStart = frameN;  // exact frame index
      
      Score.setAutoDraw(true);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    trialComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function trialRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'trial' ---
    trialComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('trial.stopped', globalClock.getTime());
    // Run 'End Routine' code from code
    if(rating.reponse){
        rating.response = parseFloat(rating.response);
    }
    
    if(decision_jar == true_jar && count != 1)
    {
        score += 10-beadnum;
    }
    thisExp.addData("DTD", beadnum);
    //thisExp.addData("Score", score);
    thisExp.addData("Arand", [A_R,A_G,A_B]);
    thisExp.addData("Brand", [B_R,B_G,B_B]);
    thisExp.addData("Decision_jar", decision_jar);
    thisExp.addData("True_jar", true_jar);
    thisExp.addData('confidence_list', confidenceRatings.join(',')); // store as comma-separated string
    thisExp.addData("Match", decision_jar===true_jar ? 1 : 0);
    thisExp.addData('currentTrial', currentTrial);
    currentTrial = currentTrial + 1;
    
    // store data for psychoJS.experiment (ExperimentHandler)
    psychoJS.experiment.addData('mouse.x', mouse.x);
    psychoJS.experiment.addData('mouse.y', mouse.y);
    psychoJS.experiment.addData('mouse.leftButton', mouse.leftButton);
    psychoJS.experiment.addData('mouse.midButton', mouse.midButton);
    psychoJS.experiment.addData('mouse.rightButton', mouse.rightButton);
    psychoJS.experiment.addData('mouse.time', mouse.time);
    psychoJS.experiment.addData('mouse.clicked_name', mouse.clicked_name);
    
    psychoJS.experiment.addData('rating.response', rating.getRating());
    psychoJS.experiment.addData('rating.rt', rating.getRT());
    psychoJS.experiment.addData('rating.history', rating.getHistory());
    // the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var itiMaxDurationReached;
var itiMaxDuration;
var itiComponents;
function itiRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'iti' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    itiClock.reset(routineTimer.getTime());
    routineTimer.add(0.300000);
    itiMaxDurationReached = false;
    // update component parameters for each repeat
    polygon.setFillColor(new util.Color([(- 1), (- 1), (- 1)]));
    psychoJS.experiment.addData('iti.started', globalClock.getTime());
    itiMaxDuration = null
    // keep track of which components have finished
    itiComponents = [];
    itiComponents.push(polygon);
    
    itiComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function itiRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'iti' ---
    // get current time
    t = itiClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *polygon* updates
    if (t >= 0.0 && polygon.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      polygon.tStart = t;  // (not accounting for frame time here)
      polygon.frameNStart = frameN;  // exact frame index
      
      polygon.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 0.3 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (polygon.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      polygon.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    itiComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function itiRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'iti' ---
    itiComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('iti.stopped', globalClock.getTime());
    if (itiMaxDurationReached) {
        itiClock.add(itiMaxDuration);
    } else {
        itiClock.add(0.300000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var thanksMaxDurationReached;
var thanksMaxDuration;
var thanksComponents;
function thanksRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'thanks' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    thanksClock.reset(routineTimer.getTime());
    routineTimer.add(2.000000);
    thanksMaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from code_thx
    
    //Change the text according to the selected language, function SetTxtThx()
    function SetTxtThx(){
        if (english){
            thx.text = "Thank you for your participation!";
        }
        else{
            thx.text = "Merci de votre participation!";
        }
    }
    
    // Compute additional scores, save them to the data file and send them to Redcap
    function GetData(){
        try{
            let data = thisExp._trialsData;
            
            /* Make array objects all have the same keys */
            let defaults = { "Language" : "", "participant" : "", "date" : "", "session": "", "expName:":"", "psychopyVersion": "", "OS": "", "frameRate": "", "mouse_instr.x" : "", 
            "mouse_instr.y" : "", "mouse_instr.leftButton" : "", "mouse_instr.midButton" : "", "mouse_instr.rightButton" : "", "mouse_instr.time": "", 
            "mouse_instr.clicked_name": "", "currentTrial": "", "Target_Distractor" : "", "Decision_jar" : "", "DTD" : "", "Match" : "", "rating.rt": "", "rating.response": "", "rating.history": ""};
            data = $.map( data, function( item ){
                return $.extend( {}, defaults, item ); 
            });
            
            // Rename "index" key to avoid errors
            data = data.map(elem => {
                elem.given_index = elem.index;
                delete elem.index;
                return elem;
            });
            
            // Create all the variables we will need
            let data2 = ["beads_orig_dtd", "beads_orig_match", "beads_orig_trial_duration", 
            "beads_orig_confidence_rating", "beads_targ_dtd", "beads_targ_match","beads_targ_confidence_rating"];
            
            for (let i = 0; i < data2.length; i++) {
                data[data2[i]] = "";
            }
            
            // Create our dataframe where we will compute all the values
            
            let df1 = new dfd.DataFrame(data);
            
            let df1_orig = df1.loc({
                rows: df1["currentTrial"].eq(1)
            });
            df1_orig.resetIndex({ inplace: true });
    
            // We will now compute the scores
            let df1_target = df1.loc({
                rows: df1["currentTrial"].gt(1).and(df1["Target_Distractor"].eq("Target"))
            });
            df1_target.resetIndex({ inplace: true });
            
            // Select rows where decision_jar is not empty so that it won't perturn following means
            let df1_target_valid = df1_target.loc({
                rows: df1_target["Decision_jar"].ne("")
            });
            df1_target_valid.resetIndex({ inplace: true });
            
            // Compute means only when it is possible and we don't have empty values
            df1["beads_orig_dtd"] = df1_orig["DTD"].values[0];
            df1["beads_orig_match"] = df1_orig["Match"].values[0];
            df1["beads_orig_trial_duration"] = df1_orig["rating.rt"].values[0];
            df1["beads_orig_confidence_rating"] = df1_orig["rating.response"].values[0];
            df1["beads_targ_dtd"] = (df1_target["DTD"]==null || df1_target["DTD"].$data.length == 0) ? "" : df1_target["DTD"].mean();
            df1["beads_targ_match"] = (df1_target["Match"]==null || df1_target["Match"].$data.length == 0) ? "" : df1_target["Match"].mean();
            df1["beads_targ_trial_duration"] = (df1_target_valid["rating.rt"]==null || df1_target_valid["rating.rt"].$data.length == 0) ? "" : df1_target_valid["rating.rt"].mean();
            df1["beads_targ_confidence_rating"] = (df1_target_valid["rating.response"]==null || df1_target_valid["rating.response"].$data.length == 0) ? "" : df1_target_valid["rating.response"].mean();
            
            //df1.print();
            //console.log("df1 orig: ", df1_orig);
            //console.log("df1 target: ", df1_target);
            //console.log("df1_target_valid: ", df1_target_valid);
            //console.log("dataframe: ", df1);
            
            let taskVersion = "Online_v3.0.2"; // Version of the task
            
            const exp_name = "BEADS";
            
            df1["date_exp"] = startingDate;
            df1["task_version"] = taskVersion;
            
            // Save dataframe inside the logfile
            psychoJS.experiment.addData('date_exp', df1["date_exp"]);
            psychoJS.experiment.addData('task_version', df1["task_version"]);
            psychoJS.experiment.addData('beads_orig_dtd', df1["beads_orig_dtd"]);
            psychoJS.experiment.addData('beads_orig_match', df1["beads_orig_match"]);
            psychoJS.experiment.addData('beads_orig_trial_duration', df1["beads_orig_trial_duration"]);
            psychoJS.experiment.addData('beads_orig_confidence_rating', df1["beads_orig_confidence_rating"]);
            psychoJS.experiment.addData('beads_targ_dtd', df1["beads_targ_dtd"]);
            psychoJS.experiment.addData('beads_targ_match', df1["beads_targ_match"]);
            psychoJS.experiment.addData('beads_targ_trial_duration', df1["beads_targ_trial_duration"]);
            psychoJS.experiment.addData('beads_targ_confidence_rating', df1["beads_targ_confidence_rating"]);
            return df1;
        }
        catch(err) {
          console.log("Error while computing the scores.");
          dumpError(err);
        }
    }
    
    function REDCapImportRecord(df1) {
        try{
          const url = 'https://portal.rimuhc.ca/cim/redcap/api/';
          let testdata;
          // Warning: If we add or remove columns in the Google file, we must also change the variables here
          testdata = [{
                    record_id: df1.loc({rows: [0], columns: ["participant"]}).values[0][0],
                    [redcapVars[1]]: df1.loc({rows: [0], columns: ["session"]}).values[0][0],
                    [redcapVars[2]]: df1["date_exp"],
                    [redcapVars[3]]: df1["task_version"],
                    [redcapVars[4]]: df1["beads_orig_dtd"],
                    [redcapVars[5]]: df1["beads_orig_match"],
                    [redcapVars[6]]: df1["beads_orig_trial_duration"],
                    [redcapVars[7]]: df1["beads_orig_confidence_rating"],
                    [redcapVars[8]]: df1["beads_targ_dtd"],
                    [redcapVars[9]]: df1["beads_targ_match"],
                    [redcapVars[10]]: df1["beads_targ_trial_duration"],
                    [redcapVars[11]]: df1["beads_targ_confidence_rating"]
          }];
          
          testdata = JSON.stringify(testdata);
          //console.log("testdata: ", testdata);
    
          const body = new FormData();
          body.append('token', redcapVars[0]);
          body.append('content', 'record');
          body.append('format', 'json');
          body.append('overwriteBehavior', 'normal');
          body.append('data', testdata);
          body.append('returnContent', 'ids');
    
          const params = {
            method: 'POST',
            body,
          }
    
        return fetch(url, params)
          .then(data => {
            console.log('fetch data: ', data)
          })
          .catch(error => console.log('Error: ', error))
     
        }
        catch(err) {
            console.log("Error while sending data to redcap: ");
            dumpError(err);
        }
    }
    
    function dumpError(err) {
      if (typeof err === 'object') {
        if (err.message) {
          console.log('\nMessage: ' + err.message);
        }
        if (err.stack) {
          console.log('\nStacktrace:');
          console.log('====================');
          console.log(err.stack);
        }
      } else {
        console.log('dumpError :: argument is not an object');
      }
    }
    
    //Call functions
    SetTxtThx();
    var res = GetData();
    REDCapImportRecord(res);
    psychoJS.experiment.addData('thanks.started', globalClock.getTime());
    thanksMaxDuration = null
    // keep track of which components have finished
    thanksComponents = [];
    thanksComponents.push(thx);
    
    thanksComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function thanksRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'thanks' ---
    // get current time
    t = thanksClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *thx* updates
    if (t >= 0.0 && thx.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      thx.tStart = t;  // (not accounting for frame time here)
      thx.frameNStart = frameN;  // exact frame index
      
      thx.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (thx.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      thx.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    thanksComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function thanksRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'thanks' ---
    thanksComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('thanks.stopped', globalClock.getTime());
    if (thanksMaxDurationReached) {
        thanksClock.add(thanksMaxDuration);
    } else {
        thanksClock.add(2.000000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  document.removeEventListener("contextmenu", preventClick, event, false);
  document.removeEventListener("contextmenu", preventClick, event, false);
  document.removeEventListener("contextmenu", preventClick, event, false);
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
