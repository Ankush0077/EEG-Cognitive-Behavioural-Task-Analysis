#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2024.2.4),
    on March 31, 2025, at 17:26
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, hardware
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER, priority)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2024.2.4'
expName = 'beads-distractor'  # from the Builder filename that created this script
# information about this experiment
expInfo = {
    'participant': '',
    'session': '001',
    'date|hid': data.getDateStr(),
    'expName|hid': expName,
    'psychopyVersion|hid': psychopyVersion,
}

# --- Define some variables which will change depending on pilot mode ---
'''
To run in pilot mode, either use the run/pilot toggle in Builder, Coder and Runner, 
or run the experiment with `--pilot` as an argument. To change what pilot 
#mode does, check out the 'Pilot mode' tab in preferences.
'''
# work out from system args whether we are running in pilot mode
PILOTING = core.setPilotModeFromArgs()
# start off with values from experiment settings
_fullScr = True
_winSize = [1680, 1050]
# if in pilot mode, apply overrides according to preferences
if PILOTING:
    # force windowed mode
    if prefs.piloting['forceWindowed']:
        _fullScr = False
        # set window size
        _winSize = prefs.piloting['forcedWindowSize']

def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # show participant info dialog
    dlg = gui.DlgFromDict(
        dictionary=expInfo, sortKeys=False, title=expName, alwaysOnTop=True
    )
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    # remove dialog-specific syntax from expInfo
    for key, val in expInfo.copy().items():
        newKey, _ = data.utils.parsePipeSyntax(key)
        expInfo[newKey] = expInfo.pop(key)
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='D:\\BSE662_Project\\beads-distractor-master\\beads-distractor_lastrun.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # set how much information should be printed to the console / app
    if PILOTING:
        logging.console.setLevel(
            prefs.piloting['pilotConsoleLoggingLevel']
        )
    else:
        logging.console.setLevel('warning')
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log')
    if PILOTING:
        logFile.setLevel(
            prefs.piloting['pilotLoggingLevel']
        )
    else:
        logFile.setLevel(
            logging.getLevel('exp')
        )
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if PILOTING:
        logging.debug('Fullscreen settings ignored as running in pilot mode.')
    
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=_winSize, fullscr=_fullScr, screen=0,
            winType='pyglet', allowGUI=False, allowStencil=False,
            monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height',
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [0,0,0]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    if expInfo is not None:
        # get/measure frame rate if not already in expInfo
        if win._monitorFrameRate is None:
            win._monitorFrameRate = win.getActualFrameRate(infoMsg='Attempting to measure frame rate of screen, please wait...')
        expInfo['frameRate'] = win._monitorFrameRate
    win.hideMessage()
    # show a visual indicator if we're in piloting mode
    if PILOTING and prefs.piloting['showPilotingIndicator']:
        win.showPilotingIndicator()
    
    return win


def setupDevices(expInfo, thisExp, win):
    """
    Setup whatever devices are available (mouse, keyboard, speaker, eyetracker, etc.) and add them to 
    the device manager (deviceManager)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    bool
        True if completed successfully.
    """
    # --- Setup input devices ---
    ioConfig = {}
    
    # Setup iohub keyboard
    ioConfig['Keyboard'] = dict(use_keymap='psychopy')
    
    # Setup iohub experiment
    ioConfig['Experiment'] = dict(filename=thisExp.dataFileName)
    
    # Start ioHub server
    ioServer = io.launchHubServer(window=win, **ioConfig)
    
    # store ioServer object in the device manager
    deviceManager.ioServer = ioServer
    
    # create a default keyboard (e.g. to check for escape)
    if deviceManager.getDevice('defaultKeyboard') is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='iohub'
        )
    # return True if completed successfully
    return True

def pauseExperiment(thisExp, win=None, timers=[], playbackComponents=[]):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    playbackComponents : list, tuple
        List of any components with a `pause` method which need to be paused.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # start a timer to figure out how long we're paused for
    pauseTimer = core.Clock()
    # pause any playback components
    for comp in playbackComponents:
        comp.pause()
    # make sure we have a keyboard
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        defaultKeyboard = deviceManager.addKeyboard(
            deviceClass='keyboard',
            deviceName='defaultKeyboard',
            backend='ioHub',
        )
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win)
        # sleep 1ms so other threads can execute
        clock.time.sleep(0.001)
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, win=win)
    # resume any playback components
    for comp in playbackComponents:
        comp.play()
    # reset any timers
    for timer in timers:
        timer.addTime(-pauseTimer.getTime())


def run(expInfo, thisExp, win, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure window is set to foreground to prevent losing focus
    win.winHandle.activate()
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = deviceManager.ioServer
    # get/create a default keyboard (e.g. to check for escape)
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='ioHub'
        )
    eyetracker = deviceManager.getDevice('eyetracker')
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "instr" ---
    # Run 'Begin Experiment' code from code_JS
    beadsImage = "beads.png"
    beads_instr = visual.ImageStim(
        win=win,
        name='beads_instr', 
        image='default.png', mask=None, anchor='center',
        ori=0, pos=(0, 0.31), draggable=False, size=[0.39,0.20],
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=512, interpolate=True, depth=-1.0)
    beadsA_instr = visual.TextStim(win=win, name='beadsA_instr',
        text='85% yellow\n15% red',
        font='Arial',
        pos=(-0.112, 0.189), draggable=False, height=0.018, wrapWidth=None, ori=0, 
        color=[-1,-1,-1], colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=-2.0);
    beadsB_instr = visual.TextStim(win=win, name='beadsB_instr',
        text='85% red\n15% yellow',
        font='Arial',
        pos=(0.105, 0.189), draggable=False, height=0.018, wrapWidth=None, ori=0, 
        color=[-1,-1,-1], colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=-3.0);
    instructionstext = visual.TextStim(win=win, name='instructionstext',
        text='In this task, you will be shown two jars full of 100 colored beads similar to those above. One jar will contain 85% beads in one color (in this case yellow), and 15% beads in another color (in this case red). The other jar will contain colored beads in the opposite ratio.\n\nFor each trial, one of the jars will be randomly selected, but you will not be told which one. The computer will randomly draw beads from the selected jar. Your job is to decide which jar the beads are being drawn from. Click the left mouse button to draw another bead and the right mouse button to make a decision.\n\nYou can continue requesting up to a certain number of beads until you feel confident about making a decision. Jars will not swap mid-game.\n\nClick on next to begin.\n',
        font='Arial',
        pos=(0, -0.135), draggable=False, height=0.029, wrapWidth=None, ori=0, 
        color=[1,1,1], colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=-4.0);
    next_instr = visual.ImageStim(
        win=win,
        name='next_instr', 
        image='button.png', mask=None, anchor='center',
        ori=0, pos=(0, -0.454), draggable=False, size=(0.25, 0.05),
        color=[1,1,1], colorSpace='rgb', opacity=0.73,
        flipHoriz=False, flipVert=False,
        texRes=512, interpolate=True, depth=-5.0)
    txt_next_instr = visual.TextStim(win=win, name='txt_next_instr',
        text='NEXT',
        font='Arial',
        pos=[0,0], draggable=False, height=0.023, wrapWidth=None, ori=0, 
        color=[-1,-1,-1], colorSpace='rgb', opacity=0.73, 
        languageStyle='LTR',
        depth=-6.0);
    mouse_instr = event.Mouse(win=win)
    x, y = [None, None]
    mouse_instr.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "trial" ---
    # Run 'Begin Experiment' code from code
    col = 'black'
    currentTrial = 1
    beadsimg1 = visual.ImageStim(
        win=win,
        name='beadsimg1', 
        image='default.png', mask=None, anchor='center',
        ori=0, pos=(0, 0.275), draggable=False, size=[0.49,0.27],
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=512, interpolate=True, depth=-1.0)
    beadstxtA = visual.TextStim(win=win, name='beadstxtA',
        text=None,
        font='Arial',
        pos=(-0.137, 0.115), draggable=False, height=0.02, wrapWidth=None, ori=0, 
        color='black', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=-2.0);
    beadstxtB = visual.TextStim(win=win, name='beadstxtB',
        text=None,
        font='Arial',
        pos=(0.135, 0.115), draggable=False, height=0.02, wrapWidth=None, ori=0, 
        color=[-1,-1,-1], colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=-3.0);
    mouse = event.Mouse(win=win)
    x, y = [None, None]
    mouse.mouseClock = core.Clock()
    bead1 = visual.ShapeStim(
        win=win, name='bead1',
        size=(0.1, 0.1), vertices='circle',
        ori=0, pos=(-0.675,0), draggable=False, anchor='center',
        lineWidth=0,
        colorSpace='rgb', lineColor=None, fillColor='white',
        opacity=1, depth=-5.0, interpolate=False)
    bead2 = visual.ShapeStim(
        win=win, name='bead2',
        size=(0.1, 0.1), vertices='circle',
        ori=0, pos=(-0.525,0), draggable=False, anchor='center',
        lineWidth=0,
        colorSpace='rgb', lineColor=None, fillColor='white',
        opacity=1, depth=-6.0, interpolate=False)
    bead3 = visual.ShapeStim(
        win=win, name='bead3',
        size=(0.1, 0.1), vertices='circle',
        ori=0, pos=(-0.375,0), draggable=False, anchor='center',
        lineWidth=0,
        colorSpace='rgb', lineColor=None, fillColor='white',
        opacity=1, depth=-7.0, interpolate=False)
    bead4 = visual.ShapeStim(
        win=win, name='bead4',
        size=(0.1, 0.1), vertices='circle',
        ori=0, pos=(-0.225, 0), draggable=False, anchor='center',
        lineWidth=0,
        colorSpace='rgb', lineColor=None, fillColor='white',
        opacity=1, depth=-8.0, interpolate=False)
    bead5 = visual.ShapeStim(
        win=win, name='bead5',
        size=(0.1, 0.1), vertices='circle',
        ori=0, pos=(-0.075, 0), draggable=False, anchor='center',
        lineWidth=0,
        colorSpace='rgb', lineColor=None, fillColor='white',
        opacity=1, depth=-9.0, interpolate=False)
    bead6 = visual.ShapeStim(
        win=win, name='bead6',
        size=(0.1, 0.1), vertices='circle',
        ori=0, pos=(0.075, 0), draggable=False, anchor='center',
        lineWidth=0,
        colorSpace='rgb', lineColor=None, fillColor='white',
        opacity=1, depth=-10.0, interpolate=False)
    bead7 = visual.ShapeStim(
        win=win, name='bead7',
        size=(0.1, 0.1), vertices='circle',
        ori=0, pos=(0.225, 0), draggable=False, anchor='center',
        lineWidth=0,
        colorSpace='rgb', lineColor=None, fillColor='white',
        opacity=1, depth=-11.0, interpolate=False)
    bead8 = visual.ShapeStim(
        win=win, name='bead8',
        size=(0.1, 0.1), vertices='circle',
        ori=0, pos=(0.375, 0), draggable=False, anchor='center',
        lineWidth=0,
        colorSpace='rgb', lineColor=None, fillColor='white',
        opacity=1, depth=-12.0, interpolate=False)
    bead9 = visual.ShapeStim(
        win=win, name='bead9',
        size=(0.1, 0.1), vertices='circle',
        ori=0, pos=(0.525, 0), draggable=False, anchor='center',
        lineWidth=0,
        colorSpace='rgb', lineColor=None, fillColor='white',
        opacity=1, depth=-13.0, interpolate=False)
    bead10 = visual.ShapeStim(
        win=win, name='bead10',
        size=(0.1, 0.1), vertices='circle',
        ori=0, pos=(0.675, 0), draggable=False, anchor='center',
        lineWidth=0,
        colorSpace='rgb', lineColor=None, fillColor='white',
        opacity=1, depth=-14.0, interpolate=False)
    ratingtext = visual.TextStim(win=win, name='ratingtext',
        text='From which jar were the beads drawn?',
        font='Arial',
        pos=(0, -0.1), draggable=False, height=0.03, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=-15.0);
    jarA = visual.ImageStim(
        win=win,
        name='jarA', 
        image='button.png', mask=None, anchor='center',
        ori=0, pos=(-0.15, -0.17), draggable=False, size=(0.17, 0.05),
        color=[1,1,1], colorSpace='rgb', opacity=0.73,
        flipHoriz=False, flipVert=False,
        texRes=512, interpolate=True, depth=-16.0)
    jarB = visual.ImageStim(
        win=win,
        name='jarB', 
        image='button.png', mask=None, anchor='center',
        ori=0, pos=(0.15, -0.17), draggable=False, size=(0.15, 0.05),
        color=[1,1,1], colorSpace='rgb', opacity=0.73,
        flipHoriz=False, flipVert=False,
        texRes=512, interpolate=True, depth=-17.0)
    jarAtext = visual.TextStim(win=win, name='jarAtext',
        text='JAR A',
        font='Arial',
        pos=[0,0], draggable=False, height=0.03, wrapWidth=None, ori=0, 
        color=[-1,-1,-1], colorSpace='rgb', opacity=0.73, 
        languageStyle='LTR',
        depth=-18.0);
    jarBtext = visual.TextStim(win=win, name='jarBtext',
        text='JAR B',
        font='Arial',
        pos=[0,0], draggable=False, height=0.03, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=0.73, 
        languageStyle='LTR',
        depth=-19.0);
    scaletext = visual.TextStim(win=win, name='scaletext',
        text='Please indicate your degree of confidence:',
        font='Arial',
        pos=(0, -0.28), draggable=False, height=0.03, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=-20.0);
    rating = visual.Slider(win=win, name='rating',
        startValue=None, size=(1,0.1), pos=(0, -0.35), units=win.units,
        labels=['0','100'], ticks=(0,100), granularity=0,
        style=['rating'], styleTweaks=(), opacity=1,
        labelColor='LightGray', markerColor='black', lineColor='White', colorSpace='rgb',
        font='Arial', labelHeight=0.05,
        flip=False, ori=0, depth=-21, readOnly=False)
    rating_value = visual.TextStim(win=win, name='rating_value',
        text=None,
        font='Arial',
        pos=(0, -0.425), draggable=False, height=0.035, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=-22.0);
    rect_draw = visual.ImageStim(
        win=win,
        name='rect_draw', 
        image='button.png', mask=None, anchor='center',
        ori=0, pos=(0, -0.17), draggable=False, size=(0.35, 0.07),
        color=[1,1,1], colorSpace='rgb', opacity=0.73,
        flipHoriz=False, flipVert=False,
        texRes=512, interpolate=True, depth=-23.0)
    rect_decide = visual.ImageStim(
        win=win,
        name='rect_decide', 
        image='button.png', mask=None, anchor='center',
        ori=0, pos=(0, -0.28), draggable=False, size=(0.35, 0.07),
        color=[1,1,1], colorSpace='rgb', opacity=0.73,
        flipHoriz=False, flipVert=False,
        texRes=512, interpolate=True, depth=-24.0)
    text_draw = visual.TextStim(win=win, name='text_draw',
        text='DRAW',
        font='Arial',
        pos=[0,0], draggable=False, height=0.025, wrapWidth=None, ori=0, 
        color=[-1,-1,-1], colorSpace='rgb', opacity=0.73, 
        languageStyle='LTR',
        depth=-25.0);
    text_decide = visual.TextStim(win=win, name='text_decide',
        text='DECIDE',
        font='Arial',
        pos=[0,0], draggable=False, height=0.025, wrapWidth=None, ori=0, 
        color=[-1,-1,-1], colorSpace='rgb', opacity=0.73, 
        languageStyle='LTR',
        depth=-26.0);
    
    # --- Initialize components for Routine "iti" ---
    polygon = visual.ShapeStim(
        win=win, name='polygon', vertices='cross',
        size=(0.1, 0.1),
        ori=0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=0,
        colorSpace='rgb', lineColor=None, fillColor='white',
        opacity=1, depth=-1.0, interpolate=False)
    
    # --- Initialize components for Routine "thanks" ---
    thx = visual.TextStim(win=win, name='thx',
        text='Thank you for participating!',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.1, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=-1.0);
    
    # create some handy timers
    
    # global clock to track the time since experiment started
    if globalClock is None:
        # create a clock if not given one
        globalClock = core.Clock()
    if isinstance(globalClock, str):
        # if given a string, make a clock accoridng to it
        if globalClock == 'float':
            # get timestamps as a simple value
            globalClock = core.Clock(format='float')
        elif globalClock == 'iso':
            # get timestamps in ISO format
            globalClock = core.Clock(format='%Y-%m-%d_%H:%M:%S.%f%z')
        else:
            # get timestamps in a custom format
            globalClock = core.Clock(format=globalClock)
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    # routine timer to track time remaining of each (possibly non-slip) routine
    routineTimer = core.Clock()
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(
        format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6
    )
    
    # --- Prepare to start Routine "instr" ---
    # create an object to store info about Routine instr
    instr = data.Routine(
        name='instr',
        components=[beads_instr, beadsA_instr, beadsB_instr, instructionstext, next_instr, txt_next_instr, mouse_instr],
    )
    instr.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_JS
    
    if english:
        instructionstext.text = instructionstext.text = "In this task, you will be shown two jars full of 100 colored beads similar to those above. One jar will contain 85% beads in one color (in this case yellow), and 15% beads in another color (in this case red). The other jar will contain colored beads in the opposite ratio.\n \n For each trial, one of the jars will be randomly selected, but you will not be told which one. The computer will randomly draw beads from the selected jar. Your job is to decide which jar the beads are being drawn from. \n \nYou can request additional beads by clicking \"Draw another bead\". If you think you know which jar was selected, click on \"Make a decision\". You can continue requesting up to a certain number of beads until you feel confident about making a decision. Jars will not swap mid-game.\n \n Click on NEXT to begin."
        beadsA_instr.text = "85% yellow \n15% red"
        beadsB_instr.text = "85% red \n15% yellow"
        txt_next_instr.text = "NEXT"
    else:
        instructionstext.text = "Dans cet exercice, nous vous montrerons deux pots remplis de 100 billes colorées similaires à ceux ci-haut. Un pot contiendra 85% de billes d’une seule couleur (dans ce cas-ci, jaune) et 15% de billes d’une autre couleur (dans ce cas-ci, rouge). L’autre pot contiendra des billes colorées dans le ratio opposé.\n \n Pour chaque essai, un des pots sera sélectionné au hasard et vous ne saurez pas lequel. L’ordinateur va piger des billes dans le pot sélectionné. Votre tâche est de décider de quel pot sont pigées les billes. \n \nVous pouvez demander des billes supplémentaires en cliquant sur \"Piger une autre bille\". Si vous pensez savoir de quel pot proviennent les billes, cliquez sur \"Faire votre choix\". Vous pouvez continuer de demander des billes jusqu’à un certain nombre pour que vous vous sentiez confiant de votre décision. Les pots ne seront pas échangés au milieu du jeu.\n \n Cliquez sur SUIVANT pour commencer."
        beadsA_instr.text = "85% jaune \n15% rouge"
        beadsB_instr.text = "85% rouge \n15% jaune"
        txt_next_instr.text = "SUIVANT"
    
    hasResources = True
    beads_instr.setImage(beadsImage)
    txt_next_instr.setPos([next_instr.pos])
    # setup some python lists for storing info about the mouse_instr
    mouse_instr.x = []
    mouse_instr.y = []
    mouse_instr.leftButton = []
    mouse_instr.midButton = []
    mouse_instr.rightButton = []
    mouse_instr.time = []
    mouse_instr.clicked_name = []
    gotValidClick = False  # until a click is received
    mouse_instr.mouseClock.reset()
    # store start times for instr
    instr.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    instr.tStart = globalClock.getTime(format='float')
    instr.status = STARTED
    thisExp.addData('instr.started', instr.tStart)
    instr.maxDuration = None
    # keep track of which components have finished
    instrComponents = instr.components
    for thisComponent in instr.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "instr" ---
    instr.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from code_JS
        # Change the color of highlighed rect
        if next_instr.contains(mouse_instr):
            next_instr.setOpacity(0.99)
            txt_next_instr.setOpacity(2)
        else:
            next_instr.setOpacity(0.73)
            txt_next_instr.setOpacity(0.73)
        
        # *beads_instr* updates
        
        # if beads_instr is starting this frame...
        if beads_instr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            beads_instr.frameNStart = frameN  # exact frame index
            beads_instr.tStart = t  # local t and not account for scr refresh
            beads_instr.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(beads_instr, 'tStartRefresh')  # time at next scr refresh
            # update status
            beads_instr.status = STARTED
            beads_instr.setAutoDraw(True)
        
        # if beads_instr is active this frame...
        if beads_instr.status == STARTED:
            # update params
            pass
        
        # *beadsA_instr* updates
        
        # if beadsA_instr is starting this frame...
        if beadsA_instr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            beadsA_instr.frameNStart = frameN  # exact frame index
            beadsA_instr.tStart = t  # local t and not account for scr refresh
            beadsA_instr.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(beadsA_instr, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'beadsA_instr.started')
            # update status
            beadsA_instr.status = STARTED
            beadsA_instr.setAutoDraw(True)
        
        # if beadsA_instr is active this frame...
        if beadsA_instr.status == STARTED:
            # update params
            pass
        
        # *beadsB_instr* updates
        
        # if beadsB_instr is starting this frame...
        if beadsB_instr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            beadsB_instr.frameNStart = frameN  # exact frame index
            beadsB_instr.tStart = t  # local t and not account for scr refresh
            beadsB_instr.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(beadsB_instr, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'beadsB_instr.started')
            # update status
            beadsB_instr.status = STARTED
            beadsB_instr.setAutoDraw(True)
        
        # if beadsB_instr is active this frame...
        if beadsB_instr.status == STARTED:
            # update params
            pass
        
        # *instructionstext* updates
        
        # if instructionstext is starting this frame...
        if instructionstext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instructionstext.frameNStart = frameN  # exact frame index
            instructionstext.tStart = t  # local t and not account for scr refresh
            instructionstext.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instructionstext, 'tStartRefresh')  # time at next scr refresh
            # update status
            instructionstext.status = STARTED
            instructionstext.setAutoDraw(True)
        
        # if instructionstext is active this frame...
        if instructionstext.status == STARTED:
            # update params
            pass
        
        # *next_instr* updates
        
        # if next_instr is starting this frame...
        if next_instr.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            next_instr.frameNStart = frameN  # exact frame index
            next_instr.tStart = t  # local t and not account for scr refresh
            next_instr.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(next_instr, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'next_instr.started')
            # update status
            next_instr.status = STARTED
            next_instr.setAutoDraw(True)
        
        # if next_instr is active this frame...
        if next_instr.status == STARTED:
            # update params
            pass
        
        # *txt_next_instr* updates
        
        # if txt_next_instr is starting this frame...
        if txt_next_instr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            txt_next_instr.frameNStart = frameN  # exact frame index
            txt_next_instr.tStart = t  # local t and not account for scr refresh
            txt_next_instr.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(txt_next_instr, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'txt_next_instr.started')
            # update status
            txt_next_instr.status = STARTED
            txt_next_instr.setAutoDraw(True)
        
        # if txt_next_instr is active this frame...
        if txt_next_instr.status == STARTED:
            # update params
            pass
        # *mouse_instr* updates
        
        # if mouse_instr is starting this frame...
        if mouse_instr.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_instr.frameNStart = frameN  # exact frame index
            mouse_instr.tStart = t  # local t and not account for scr refresh
            mouse_instr.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_instr, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse_instr.started', t)
            # update status
            mouse_instr.status = STARTED
            prevButtonState = mouse_instr.getPressed()  # if button is down already this ISN'T a new click
        if mouse_instr.status == STARTED:  # only update if started and not finished!
            buttons = mouse_instr.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    clickableList = environmenttools.getFromNames(next_instr, namespace=locals())
                    for obj in clickableList:
                        # is this object clicked on?
                        if obj.contains(mouse_instr):
                            gotValidClick = True
                            mouse_instr.clicked_name.append(obj.name)
                    if not gotValidClick:
                        mouse_instr.clicked_name.append(None)
                    x, y = mouse_instr.getPos()
                    mouse_instr.x.append(x)
                    mouse_instr.y.append(y)
                    buttons = mouse_instr.getPressed()
                    mouse_instr.leftButton.append(buttons[0])
                    mouse_instr.midButton.append(buttons[1])
                    mouse_instr.rightButton.append(buttons[2])
                    mouse_instr.time.append(mouse_instr.mouseClock.getTime())
                    if gotValidClick:
                        continueRoutine = False  # end routine on response
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            instr.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instr.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instr" ---
    for thisComponent in instr.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for instr
    instr.tStop = globalClock.getTime(format='float')
    instr.tStopRefresh = tThisFlipGlobal
    thisExp.addData('instr.stopped', instr.tStop)
    # store data for thisExp (ExperimentHandler)
    thisExp.addData('mouse_instr.x', mouse_instr.x)
    thisExp.addData('mouse_instr.y', mouse_instr.y)
    thisExp.addData('mouse_instr.leftButton', mouse_instr.leftButton)
    thisExp.addData('mouse_instr.midButton', mouse_instr.midButton)
    thisExp.addData('mouse_instr.rightButton', mouse_instr.rightButton)
    thisExp.addData('mouse_instr.time', mouse_instr.time)
    thisExp.addData('mouse_instr.clicked_name', mouse_instr.clicked_name)
    thisExp.nextEntry()
    # the Routine "instr" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler2(
        name='trials',
        nReps=1.0, 
        method='sequential', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions(trialConditions), 
        seed=None, 
    )
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            globals()[paramName] = thisTrial[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisTrial in trials:
        currentLoop = trials
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                globals()[paramName] = thisTrial[paramName]
        
        # --- Prepare to start Routine "trial" ---
        # create an object to store info about Routine trial
        trial = data.Routine(
            name='trial',
            components=[beadsimg1, beadstxtA, beadstxtB, mouse, bead1, bead2, bead3, bead4, bead5, bead6, bead7, bead8, bead9, bead10, ratingtext, jarA, jarB, jarAtext, jarBtext, scaletext, rating, rating_value, rect_draw, rect_decide, text_draw, text_decide],
        )
        trial.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code
        import random
        
        #declare variables
        mouse_clicked = False
        select_decide = False
        jarpic = jarPicture
        ratingClick = 0
        ratingstart = False
        ratingdone = False
        beadnum = 1
        beads = [bead1, bead2, bead3, bead4, bead5, bead6, bead7, bead8, bead9, bead10]
        beadcolours = []
        true_jar = "jarA"
        rating_is_initialized = False
        decision_jar = ""
        
        #Jars texts
        colorA_1 = txt_1
        colorA_2 = txt_2
        colorB_1 = txt_3
        colorB_2 = txt_4
        
        beadstxtA.text = colorA_1 +'\n'+colorA_2
        beadstxtB.text = colorB_1 +'\n'+colorB_2
        
        #define slider marker and colour
        rating = visual.Slider(win=win, name='rating', size=(1.0, 0.05), pos=(0, -0.35), labels=("0%", "100%"), ticks=(0, 100), granularity=0, style=("rating"), color=(0.65, 0.65, 0.65), font='Arial', flip = False, labelHeight= 0.05)
        #rating.size[1] = rating.size[1] / 2;
        
        #randomize beads and colours
        if random.random() > 0.5:
            true_jar = "jarB"
            [A_R, A_G, A_B, B_R, B_G, B_B] = [B_R, B_G, B_B, A_R, A_G, A_B]
            
        for i in range(0, len(beads)):
            if colorSequence[i] == "A":
                beadcolours.append([A_R,A_G,A_B])
            elif colorSequence[i] == "B":
                beadcolours.append([B_R,B_G,B_B])
            i += 1
        
        #Change the text according to the selected language
        if english:
            ratingtext.text = "From which jar were the beads drawn?"
            jarAtext.text = "JAR A"
            jarBtext.text = "JAR B"
            scaletext.text = "Please indicate your degree of confidence:"
            text_draw.text = "DRAW ANOTHER BEAD"
            text_decide.text = "MAKE A DECISION"
        else:
            ratingtext.text = "De quel pot viennent les billes?"
            jarAtext.text = "POT A"
            jarBtext.text = "POT B"
            scaletext.text = "S’il vous plaît, veuillez évaluer votre degré de confiance :"
            text_draw.text = "PIGER UNE AUTRE BILLE"
            text_decide.text = "FAIRE VOTRE CHOIX"
        beadsimg1.setImage(jarpic)
        # setup some python lists for storing info about the mouse
        mouse.x = []
        mouse.y = []
        mouse.leftButton = []
        mouse.midButton = []
        mouse.rightButton = []
        mouse.time = []
        mouse.clicked_name = []
        gotValidClick = False  # until a click is received
        mouse.mouseClock.reset()
        bead1.setFillColor([0,0,0])
        bead2.setFillColor([0,0,0])
        bead3.setFillColor([0,0,0])
        bead4.setFillColor([0,0,0])
        bead5.setFillColor([0,0,0])
        bead6.setFillColor([0,0,0])
        bead7.setFillColor([0,0,0])
        bead8.setFillColor([0,0,0])
        bead9.setFillColor([0,0,0])
        bead10.setFillColor([0,0,0])
        jarAtext.setPos([jarA.pos])
        jarBtext.setColor([-1,-1,-1], colorSpace='rgb')
        jarBtext.setPos([jarB.pos])
        rating.reset()
        rating_value.setText('')
        text_draw.setPos([rect_draw.pos])
        text_decide.setPos([rect_decide.pos])
        # store start times for trial
        trial.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        trial.tStart = globalClock.getTime(format='float')
        trial.status = STARTED
        thisExp.addData('trial.started', trial.tStart)
        trial.maxDuration = None
        # keep track of which components have finished
        trialComponents = trial.components
        for thisComponent in trial.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "trial" ---
        # if trial has changed, end Routine now
        if isinstance(trials, data.TrialHandler2) and thisTrial.thisN != trials.thisTrial.thisN:
            continueRoutine = False
        trial.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from code
            #first bead appears right away
            bead1.setColor(beadcolours[1])
            
            #modify slider marker and colour
            if rating_is_initialized == False:
                try:
                    rating.marker.setColor(col, colorSpace='rgb')
                    rating._barSize = (1, 0.01)
                    rating._onChange(True)()
                    rating._setupSlider()
                except:
                    print("An exception while modifying slider")
                rating_is_initialized = True
            
            #display rating value
            if rating.markerPos != 0 and rating.markerPos != None:
                rating_value.text = str(int(round(rating.markerPos)))
            
            #show jar selection
            if select_decide == True and ratingdone == False and (mouse.getPressed()[0] == True and jarA.contains(mouse)):
                decision_jar = "jarA"
                ratingstart = True
            
            if select_decide == True and ratingdone == False and (mouse.getPressed()[0] == True and jarB.contains(mouse)):
                decision_jar = "jarB"
                ratingstart = True
                
            #As soon as the rating of the confidence is done, the participants can no longer change the selected jar
            if rating.getRating() != None:
                ratingdone = True
                
            #move to next trial after rating + 1 second (allow for change in ratings within 1 second)
            if rating.getRating() != None and routineTimer.getTime() > rating.getRT() + 1 and rating.getRating() == rating.markerPos:
                continueRoutine = False
            
            #Change the color of highlighed rect
            if rect_draw.contains(mouse):
                rect_draw.opacity = 0.99
                text_draw.opacity = 2
            else:
                rect_draw.opacity = 0.73
                text_draw.opacity = 0.73
            if rect_decide.contains(mouse):
                rect_decide.opacity = 0.99
                text_decide.opacity = 2
            else:
                rect_decide.opacity = 0.73
                text_decide.opacity = 0.73
            
            #Change the color of highlighed rect. We won't highligh if participant can not rate anymore 
            if ratingdone == False:
                if jarA.contains(mouse):
                    jarA.opacity = 0.99
                    jarAtext.opacity = 2
                else:
                    jarA.opacity = 0.73
                    jarAtext.opacity = 0.73
                if jarB.contains(mouse):
                    jarB.opacity = 0.99
                    jarBtext.opacity = 2
                else:
                    jarB.opacity = 0.73
                    jarBtext.opacity = 0.73
            
            if select_decide == False and rect_draw.contains(mouse) and mouse.getPressed()[0] == True:
                if mouse_clicked == False:
                    mouse_clicked = True
                    if beadnum == 10:
                        beadnum = 11
                        continueRoutine = False
                    else:
                        beads[beadnum].setColor(beadcolours[beadnum])
                        beadnum += 1
            else:
                mouse_clicked = False
            
            if rect_decide.contains(mouse) and mouse.getPressed()[0] == True:
                select_decide = True
            
            # *beadsimg1* updates
            
            # if beadsimg1 is starting this frame...
            if beadsimg1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                beadsimg1.frameNStart = frameN  # exact frame index
                beadsimg1.tStart = t  # local t and not account for scr refresh
                beadsimg1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(beadsimg1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'beadsimg1.started')
                # update status
                beadsimg1.status = STARTED
                beadsimg1.setAutoDraw(True)
            
            # if beadsimg1 is active this frame...
            if beadsimg1.status == STARTED:
                # update params
                pass
            
            # *beadstxtA* updates
            
            # if beadstxtA is starting this frame...
            if beadstxtA.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                beadstxtA.frameNStart = frameN  # exact frame index
                beadstxtA.tStart = t  # local t and not account for scr refresh
                beadstxtA.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(beadstxtA, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'beadstxtA.started')
                # update status
                beadstxtA.status = STARTED
                beadstxtA.setAutoDraw(True)
            
            # if beadstxtA is active this frame...
            if beadstxtA.status == STARTED:
                # update params
                pass
            
            # *beadstxtB* updates
            
            # if beadstxtB is starting this frame...
            if beadstxtB.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                beadstxtB.frameNStart = frameN  # exact frame index
                beadstxtB.tStart = t  # local t and not account for scr refresh
                beadstxtB.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(beadstxtB, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'beadstxtB.started')
                # update status
                beadstxtB.status = STARTED
                beadstxtB.setAutoDraw(True)
            
            # if beadstxtB is active this frame...
            if beadstxtB.status == STARTED:
                # update params
                pass
            # *mouse* updates
            
            # if mouse is starting this frame...
            if mouse.status == NOT_STARTED and t >= 0-frameTolerance:
                # keep track of start time/frame for later
                mouse.frameNStart = frameN  # exact frame index
                mouse.tStart = t  # local t and not account for scr refresh
                mouse.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
                # update status
                mouse.status = STARTED
                prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
            if mouse.status == STARTED:  # only update if started and not finished!
                buttons = mouse.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        clickableList = environmenttools.getFromNames([jarA,jarB,rect_draw,rect_decide], namespace=locals())
                        for obj in clickableList:
                            # is this object clicked on?
                            if obj.contains(mouse):
                                gotValidClick = True
                                mouse.clicked_name.append(obj.name)
                        if not gotValidClick:
                            mouse.clicked_name.append(None)
                        x, y = mouse.getPos()
                        mouse.x.append(x)
                        mouse.y.append(y)
                        buttons = mouse.getPressed()
                        mouse.leftButton.append(buttons[0])
                        mouse.midButton.append(buttons[1])
                        mouse.rightButton.append(buttons[2])
                        mouse.time.append(mouse.mouseClock.getTime())
            
            # *bead1* updates
            
            # if bead1 is starting this frame...
            if bead1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                bead1.frameNStart = frameN  # exact frame index
                bead1.tStart = t  # local t and not account for scr refresh
                bead1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(bead1, 'tStartRefresh')  # time at next scr refresh
                # update status
                bead1.status = STARTED
                bead1.setAutoDraw(True)
            
            # if bead1 is active this frame...
            if bead1.status == STARTED:
                # update params
                pass
            
            # *bead2* updates
            
            # if bead2 is starting this frame...
            if bead2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                bead2.frameNStart = frameN  # exact frame index
                bead2.tStart = t  # local t and not account for scr refresh
                bead2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(bead2, 'tStartRefresh')  # time at next scr refresh
                # update status
                bead2.status = STARTED
                bead2.setAutoDraw(True)
            
            # if bead2 is active this frame...
            if bead2.status == STARTED:
                # update params
                pass
            
            # *bead3* updates
            
            # if bead3 is starting this frame...
            if bead3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                bead3.frameNStart = frameN  # exact frame index
                bead3.tStart = t  # local t and not account for scr refresh
                bead3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(bead3, 'tStartRefresh')  # time at next scr refresh
                # update status
                bead3.status = STARTED
                bead3.setAutoDraw(True)
            
            # if bead3 is active this frame...
            if bead3.status == STARTED:
                # update params
                pass
            
            # *bead4* updates
            
            # if bead4 is starting this frame...
            if bead4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                bead4.frameNStart = frameN  # exact frame index
                bead4.tStart = t  # local t and not account for scr refresh
                bead4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(bead4, 'tStartRefresh')  # time at next scr refresh
                # update status
                bead4.status = STARTED
                bead4.setAutoDraw(True)
            
            # if bead4 is active this frame...
            if bead4.status == STARTED:
                # update params
                pass
            
            # *bead5* updates
            
            # if bead5 is starting this frame...
            if bead5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                bead5.frameNStart = frameN  # exact frame index
                bead5.tStart = t  # local t and not account for scr refresh
                bead5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(bead5, 'tStartRefresh')  # time at next scr refresh
                # update status
                bead5.status = STARTED
                bead5.setAutoDraw(True)
            
            # if bead5 is active this frame...
            if bead5.status == STARTED:
                # update params
                pass
            
            # *bead6* updates
            
            # if bead6 is starting this frame...
            if bead6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                bead6.frameNStart = frameN  # exact frame index
                bead6.tStart = t  # local t and not account for scr refresh
                bead6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(bead6, 'tStartRefresh')  # time at next scr refresh
                # update status
                bead6.status = STARTED
                bead6.setAutoDraw(True)
            
            # if bead6 is active this frame...
            if bead6.status == STARTED:
                # update params
                pass
            
            # *bead7* updates
            
            # if bead7 is starting this frame...
            if bead7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                bead7.frameNStart = frameN  # exact frame index
                bead7.tStart = t  # local t and not account for scr refresh
                bead7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(bead7, 'tStartRefresh')  # time at next scr refresh
                # update status
                bead7.status = STARTED
                bead7.setAutoDraw(True)
            
            # if bead7 is active this frame...
            if bead7.status == STARTED:
                # update params
                pass
            
            # *bead8* updates
            
            # if bead8 is starting this frame...
            if bead8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                bead8.frameNStart = frameN  # exact frame index
                bead8.tStart = t  # local t and not account for scr refresh
                bead8.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(bead8, 'tStartRefresh')  # time at next scr refresh
                # update status
                bead8.status = STARTED
                bead8.setAutoDraw(True)
            
            # if bead8 is active this frame...
            if bead8.status == STARTED:
                # update params
                pass
            
            # *bead9* updates
            
            # if bead9 is starting this frame...
            if bead9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                bead9.frameNStart = frameN  # exact frame index
                bead9.tStart = t  # local t and not account for scr refresh
                bead9.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(bead9, 'tStartRefresh')  # time at next scr refresh
                # update status
                bead9.status = STARTED
                bead9.setAutoDraw(True)
            
            # if bead9 is active this frame...
            if bead9.status == STARTED:
                # update params
                pass
            
            # *bead10* updates
            
            # if bead10 is starting this frame...
            if bead10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                bead10.frameNStart = frameN  # exact frame index
                bead10.tStart = t  # local t and not account for scr refresh
                bead10.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(bead10, 'tStartRefresh')  # time at next scr refresh
                # update status
                bead10.status = STARTED
                bead10.setAutoDraw(True)
            
            # if bead10 is active this frame...
            if bead10.status == STARTED:
                # update params
                pass
            
            # *ratingtext* updates
            
            # if ratingtext is starting this frame...
            if ratingtext.status == NOT_STARTED and select_decide == 1:
                # keep track of start time/frame for later
                ratingtext.frameNStart = frameN  # exact frame index
                ratingtext.tStart = t  # local t and not account for scr refresh
                ratingtext.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ratingtext, 'tStartRefresh')  # time at next scr refresh
                # update status
                ratingtext.status = STARTED
                ratingtext.setAutoDraw(True)
            
            # if ratingtext is active this frame...
            if ratingtext.status == STARTED:
                # update params
                pass
            
            # *jarA* updates
            
            # if jarA is starting this frame...
            if jarA.status == NOT_STARTED and select_decide == 1:
                # keep track of start time/frame for later
                jarA.frameNStart = frameN  # exact frame index
                jarA.tStart = t  # local t and not account for scr refresh
                jarA.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(jarA, 'tStartRefresh')  # time at next scr refresh
                # update status
                jarA.status = STARTED
                jarA.setAutoDraw(True)
            
            # if jarA is active this frame...
            if jarA.status == STARTED:
                # update params
                pass
            
            # *jarB* updates
            
            # if jarB is starting this frame...
            if jarB.status == NOT_STARTED and select_decide == 1:
                # keep track of start time/frame for later
                jarB.frameNStart = frameN  # exact frame index
                jarB.tStart = t  # local t and not account for scr refresh
                jarB.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(jarB, 'tStartRefresh')  # time at next scr refresh
                # update status
                jarB.status = STARTED
                jarB.setAutoDraw(True)
            
            # if jarB is active this frame...
            if jarB.status == STARTED:
                # update params
                pass
            
            # *jarAtext* updates
            
            # if jarAtext is starting this frame...
            if jarAtext.status == NOT_STARTED and select_decide == 1:
                # keep track of start time/frame for later
                jarAtext.frameNStart = frameN  # exact frame index
                jarAtext.tStart = t  # local t and not account for scr refresh
                jarAtext.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(jarAtext, 'tStartRefresh')  # time at next scr refresh
                # update status
                jarAtext.status = STARTED
                jarAtext.setAutoDraw(True)
            
            # if jarAtext is active this frame...
            if jarAtext.status == STARTED:
                # update params
                pass
            
            # *jarBtext* updates
            
            # if jarBtext is starting this frame...
            if jarBtext.status == NOT_STARTED and select_decide == 1:
                # keep track of start time/frame for later
                jarBtext.frameNStart = frameN  # exact frame index
                jarBtext.tStart = t  # local t and not account for scr refresh
                jarBtext.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(jarBtext, 'tStartRefresh')  # time at next scr refresh
                # update status
                jarBtext.status = STARTED
                jarBtext.setAutoDraw(True)
            
            # if jarBtext is active this frame...
            if jarBtext.status == STARTED:
                # update params
                pass
            
            # *scaletext* updates
            
            # if scaletext is starting this frame...
            if scaletext.status == NOT_STARTED and ratingstart == 1:
                # keep track of start time/frame for later
                scaletext.frameNStart = frameN  # exact frame index
                scaletext.tStart = t  # local t and not account for scr refresh
                scaletext.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(scaletext, 'tStartRefresh')  # time at next scr refresh
                # update status
                scaletext.status = STARTED
                scaletext.setAutoDraw(True)
            
            # if scaletext is active this frame...
            if scaletext.status == STARTED:
                # update params
                pass
            
            # *rating* updates
            
            # if rating is starting this frame...
            if rating.status == NOT_STARTED and ratingstart == 1:
                # keep track of start time/frame for later
                rating.frameNStart = frameN  # exact frame index
                rating.tStart = t  # local t and not account for scr refresh
                rating.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rating, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'rating.started')
                # update status
                rating.status = STARTED
                rating.setAutoDraw(True)
            
            # if rating is active this frame...
            if rating.status == STARTED:
                # update params
                pass
            
            # *rating_value* updates
            
            # if rating_value is starting this frame...
            if rating_value.status == NOT_STARTED and ratingstart == 1:
                # keep track of start time/frame for later
                rating_value.frameNStart = frameN  # exact frame index
                rating_value.tStart = t  # local t and not account for scr refresh
                rating_value.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rating_value, 'tStartRefresh')  # time at next scr refresh
                # update status
                rating_value.status = STARTED
                rating_value.setAutoDraw(True)
            
            # if rating_value is active this frame...
            if rating_value.status == STARTED:
                # update params
                pass
            
            # *rect_draw* updates
            
            # if rect_draw is starting this frame...
            if rect_draw.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                rect_draw.frameNStart = frameN  # exact frame index
                rect_draw.tStart = t  # local t and not account for scr refresh
                rect_draw.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rect_draw, 'tStartRefresh')  # time at next scr refresh
                # update status
                rect_draw.status = STARTED
                rect_draw.setAutoDraw(True)
            
            # if rect_draw is active this frame...
            if rect_draw.status == STARTED:
                # update params
                pass
            
            # if rect_draw is stopping this frame...
            if rect_draw.status == STARTED:
                if bool(select_decide == 1):
                    # keep track of stop time/frame for later
                    rect_draw.tStop = t  # not accounting for scr refresh
                    rect_draw.tStopRefresh = tThisFlipGlobal  # on global time
                    rect_draw.frameNStop = frameN  # exact frame index
                    # update status
                    rect_draw.status = FINISHED
                    rect_draw.setAutoDraw(False)
            
            # *rect_decide* updates
            
            # if rect_decide is starting this frame...
            if rect_decide.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                rect_decide.frameNStart = frameN  # exact frame index
                rect_decide.tStart = t  # local t and not account for scr refresh
                rect_decide.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rect_decide, 'tStartRefresh')  # time at next scr refresh
                # update status
                rect_decide.status = STARTED
                rect_decide.setAutoDraw(True)
            
            # if rect_decide is active this frame...
            if rect_decide.status == STARTED:
                # update params
                pass
            
            # if rect_decide is stopping this frame...
            if rect_decide.status == STARTED:
                if bool(select_decide == 1):
                    # keep track of stop time/frame for later
                    rect_decide.tStop = t  # not accounting for scr refresh
                    rect_decide.tStopRefresh = tThisFlipGlobal  # on global time
                    rect_decide.frameNStop = frameN  # exact frame index
                    # update status
                    rect_decide.status = FINISHED
                    rect_decide.setAutoDraw(False)
            
            # *text_draw* updates
            
            # if text_draw is starting this frame...
            if text_draw.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_draw.frameNStart = frameN  # exact frame index
                text_draw.tStart = t  # local t and not account for scr refresh
                text_draw.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_draw, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_draw.started')
                # update status
                text_draw.status = STARTED
                text_draw.setAutoDraw(True)
            
            # if text_draw is active this frame...
            if text_draw.status == STARTED:
                # update params
                pass
            
            # if text_draw is stopping this frame...
            if text_draw.status == STARTED:
                if bool(select_decide == 1):
                    # keep track of stop time/frame for later
                    text_draw.tStop = t  # not accounting for scr refresh
                    text_draw.tStopRefresh = tThisFlipGlobal  # on global time
                    text_draw.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_draw.stopped')
                    # update status
                    text_draw.status = FINISHED
                    text_draw.setAutoDraw(False)
            
            # *text_decide* updates
            
            # if text_decide is starting this frame...
            if text_decide.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_decide.frameNStart = frameN  # exact frame index
                text_decide.tStart = t  # local t and not account for scr refresh
                text_decide.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_decide, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_decide.started')
                # update status
                text_decide.status = STARTED
                text_decide.setAutoDraw(True)
            
            # if text_decide is active this frame...
            if text_decide.status == STARTED:
                # update params
                pass
            
            # if text_decide is stopping this frame...
            if text_decide.status == STARTED:
                if bool(select_decide == 1):
                    # keep track of stop time/frame for later
                    text_decide.tStop = t  # not accounting for scr refresh
                    text_decide.tStopRefresh = tThisFlipGlobal  # on global time
                    text_decide.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_decide.stopped')
                    # update status
                    text_decide.status = FINISHED
                    text_decide.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                trial.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trial.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "trial" ---
        for thisComponent in trial.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for trial
        trial.tStop = globalClock.getTime(format='float')
        trial.tStopRefresh = tThisFlipGlobal
        thisExp.addData('trial.stopped', trial.tStop)
        # Run 'End Routine' code from code
        thisExp.addData('DTD', beadnum)
        thisExp.addData('Arand', [A_R,A_G,A_B])
        thisExp.addData('Brand', [B_R,B_G,B_B])
        thisExp.addData("Decision_jar", decision_jar)
        thisExp.addData("True_jar", true_jar)
        if decision_jar == true_jar:
            thisExp.addData("Match", 1)
        else:
            thisExp.addData("Match", 0)
        thisExp.addData('currentTrial', currentTrial)
        currentTrial = currentTrial + 1
        # store data for trials (TrialHandler)
        trials.addData('mouse.x', mouse.x)
        trials.addData('mouse.y', mouse.y)
        trials.addData('mouse.leftButton', mouse.leftButton)
        trials.addData('mouse.midButton', mouse.midButton)
        trials.addData('mouse.rightButton', mouse.rightButton)
        trials.addData('mouse.time', mouse.time)
        trials.addData('mouse.clicked_name', mouse.clicked_name)
        trials.addData('rating.response', rating.getRating())
        trials.addData('rating.rt', rating.getRT())
        trials.addData('rating.history', rating.getHistory())
        # the Routine "trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "iti" ---
        # create an object to store info about Routine iti
        iti = data.Routine(
            name='iti',
            components=[polygon],
        )
        iti.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_iti
        # Avoid displaying the fixation cross if we finished displaying the trials
        if trials.nRemaining == 0:
            continueRoutine = False
        polygon.setFillColor([-1,-1,-1])
        # store start times for iti
        iti.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        iti.tStart = globalClock.getTime(format='float')
        iti.status = STARTED
        thisExp.addData('iti.started', iti.tStart)
        iti.maxDuration = None
        # keep track of which components have finished
        itiComponents = iti.components
        for thisComponent in iti.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "iti" ---
        # if trial has changed, end Routine now
        if isinstance(trials, data.TrialHandler2) and thisTrial.thisN != trials.thisTrial.thisN:
            continueRoutine = False
        iti.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.5:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *polygon* updates
            
            # if polygon is starting this frame...
            if polygon.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                polygon.frameNStart = frameN  # exact frame index
                polygon.tStart = t  # local t and not account for scr refresh
                polygon.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(polygon, 'tStartRefresh')  # time at next scr refresh
                # update status
                polygon.status = STARTED
                polygon.setAutoDraw(True)
            
            # if polygon is active this frame...
            if polygon.status == STARTED:
                # update params
                pass
            
            # if polygon is stopping this frame...
            if polygon.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > polygon.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    polygon.tStop = t  # not accounting for scr refresh
                    polygon.tStopRefresh = tThisFlipGlobal  # on global time
                    polygon.frameNStop = frameN  # exact frame index
                    # update status
                    polygon.status = FINISHED
                    polygon.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                iti.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in iti.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "iti" ---
        for thisComponent in iti.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for iti
        iti.tStop = globalClock.getTime(format='float')
        iti.tStopRefresh = tThisFlipGlobal
        thisExp.addData('iti.stopped', iti.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if iti.maxDurationReached:
            routineTimer.addTime(-iti.maxDuration)
        elif iti.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.500000)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'trials'
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "thanks" ---
    # create an object to store info about Routine thanks
    thanks = data.Routine(
        name='thanks',
        components=[thx],
    )
    thanks.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_thx
    import traceback
    
    #Change the text according to the selected language, function SetTxtInstr2()
    if english:
        thx.text = "Thank you for your participation!"
    else:
        thx.text = "Merci de votre participation!"
    
    #Get Data
    try:
        df1 = pd.DataFrame.from_dict(thisExp.getAllEntries())
    
        # Create all the variables we will need
        df1 = df1.assign(beads_orig_dtd="", beads_orig_match="", 
        beads_orig_trial_duration="", beads_orig_confidence_rating="", 
        beads_targ_dtd="", beads_targ_match="", 
        beads_targ_trial_duration="", beads_targ_confidence_rating="")
        
        #Select first trial that is a testing one
        df1_orig = df1.query('currentTrial == 1')
        df1_orig.reset_index(drop=True, inplace=True) #indexing was a concern in some calculations.
        
        #We will now compute the scores
        df1["beads_orig_dtd"] = df1_orig["DTD"]
        df1["beads_orig_match"] = df1_orig["Match"]
        df1["beads_orig_trial_duration"] = df1_orig['rating.rt']
        df1["beads_orig_confidence_rating"] = df1_orig["rating.response"]
    
        #Select target trials
        df1_target = df1.query('currentTrial > 1 and Target_Distractor == "Target"')
        df1_target.reset_index(drop=True, inplace=True)
        
        df1["beads_targ_dtd"] = df1_target['DTD'].mean()
        df1["beads_targ_match"] = df1_target['Match'].mean()
        
        #Remove rows where decision_jar is empty so that it won't perturn following means
        clean_df1_target = df1_target[df1_target.Decision_jar != ""]
        clean_df1_target.reset_index(drop=True, inplace=True)
        
        df1["beads_targ_trial_duration"] = clean_df1_target['rating.rt'].mean()
        df1["beads_targ_confidence_rating"] = clean_df1_target['rating.response'].mean()
    
        # Remove nan values if we have any (e.g., no orig confidence rating)
        df1 = df1.fillna('')
    
        # Save task version and date
        taskVersion = "Offline_v3.0.2"
        df1["date_exp"] = startingDate
        df1["task_version"] = taskVersion
        
        #print("df1", df1.to_string().encode('utf-8'))
        #print("columns ", df1.columns)
        #print("df1 size: ", df1.size)
    
        thisExp.addData('date_exp', df1["date_exp"].iloc[0])
        thisExp.addData('task_version', df1["task_version"].iloc[0])
        thisExp.addData('beads_orig_dtd', df1["beads_orig_dtd"].iloc[0])
        thisExp.addData('beads_orig_match', df1["beads_orig_match"].iloc[0])
        thisExp.addData('beads_orig_trial_duration', df1["beads_orig_trial_duration"].iloc[0])
        thisExp.addData('beads_orig_confidence_rating', df1["beads_orig_confidence_rating"].iloc[0])
        thisExp.addData('beads_targ_dtd', df1["beads_targ_dtd"].iloc[0])
        thisExp.addData('beads_targ_match', df1["beads_targ_match"].iloc[0])
        thisExp.addData('beads_targ_trial_duration', df1["beads_targ_trial_duration"].iloc[0])
        thisExp.addData('beads_targ_confidence_rating', df1["beads_targ_confidence_rating"].iloc[0])
    except Exception:
        print("An exception occurred. Error while computing scores.")
        traceback.print_exc()
        
    # Send data to redcap
    try:
        import requests, hashlib
        # Transform data to JSON Format
        # If we add or remove columns in the Google file, we must also change the variables here
        myDict = {}
        myDict["record_id"] = df1['participant'].iloc[0]
        myDict[redcapVars[1]] = df1['session'].iloc[0]
        myDict[redcapVars[2]] = df1['date_exp'].iloc[0]
        myDict[redcapVars[3]] = df1['task_version'].iloc[0]
        myDict[redcapVars[4]] = df1['beads_orig_dtd'].iloc[0]
        myDict[redcapVars[5]] = df1['beads_orig_match'].iloc[0]
        myDict[redcapVars[6]] = df1['beads_orig_trial_duration'].iloc[0]
        myDict[redcapVars[7]] = df1['beads_orig_confidence_rating'].iloc[0]
        myDict[redcapVars[8]] = df1['beads_targ_dtd'].iloc[0]
        myDict[redcapVars[9]] = df1['beads_targ_match'].iloc[0]
        myDict[redcapVars[10]] = df1['beads_targ_trial_duration'].iloc[0]
        myDict[redcapVars[11]] = df1['beads_targ_confidence_rating'].iloc[0]
        
        data_to_send = [myDict]
        
        #print("data to send: ", data_to_send)
        
        url = 'https://portal.rimuhc.ca/cim/redcap/api/'
        redcap_data = {
            'token': redcapVars[0],
            'content': 'record',
            'format': 'json',
            'type': 'flat',
            'overwriteBehavior': 'normal',
            'forceAutoNumber': 'false',
            'data': json.dumps(data_to_send),
            'returnContent': 'ids',
            'returnFormat': 'json',
            'record_id': hashlib.sha1().hexdigest()[:16]
        }
        x = requests.post(url, data = redcap_data)
        print(x.text)
        print("Data sent to redcap.")
    except Exception:
        print("An exception occurred. Error while sending data to redcap.")
        traceback.print_exc()
    # store start times for thanks
    thanks.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    thanks.tStart = globalClock.getTime(format='float')
    thanks.status = STARTED
    thisExp.addData('thanks.started', thanks.tStart)
    thanks.maxDuration = None
    # keep track of which components have finished
    thanksComponents = thanks.components
    for thisComponent in thanks.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "thanks" ---
    thanks.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 2.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *thx* updates
        
        # if thx is starting this frame...
        if thx.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            thx.frameNStart = frameN  # exact frame index
            thx.tStart = t  # local t and not account for scr refresh
            thx.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(thx, 'tStartRefresh')  # time at next scr refresh
            # update status
            thx.status = STARTED
            thx.setAutoDraw(True)
        
        # if thx is active this frame...
        if thx.status == STARTED:
            # update params
            pass
        
        # if thx is stopping this frame...
        if thx.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > thx.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                thx.tStop = t  # not accounting for scr refresh
                thx.tStopRefresh = tThisFlipGlobal  # on global time
                thx.frameNStop = frameN  # exact frame index
                # update status
                thx.status = FINISHED
                thx.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            thanks.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in thanks.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "thanks" ---
    for thisComponent in thanks.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for thanks
    thanks.tStop = globalClock.getTime(format='float')
    thanks.tStopRefresh = tThisFlipGlobal
    thisExp.addData('thanks.stopped', thanks.tStop)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if thanks.maxDurationReached:
        routineTimer.addTime(-thanks.maxDuration)
    elif thanks.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-2.000000)
    thisExp.nextEntry()
    
    # mark experiment as finished
    endExperiment(thisExp, win=win)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # return console logger level to WARNING
    logging.console.setLevel(logging.WARNING)
    # mark experiment handler as finished
    thisExp.status = FINISHED
    logging.flush()


def quit(thisExp, win=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    setupDevices(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win,
        globalClock='float'
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win)
