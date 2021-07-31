import PySimpleGUI as sg
import os
import Scene
import xml.etree.ElementTree as ET


# Functions :D
def updateSceneList():
    global scenesOrdered
    global sceneListBox
    sceneList = []
    i = 1

    for sc in scenesOrdered:
        sceneList.append(sc.getName())
        i = i + 1

    sceneListBox.update(sceneList)


def save(file_name):
    global scenesOrdered
    root = ET.Element('DR_Text')
    sceneBase = ET.SubElement(root, "scenes")
    sceneBase.set("count", str(len(scenesOrdered)))
    for scene in scenesOrdered:
        sceneElement = ET.SubElement(sceneBase, "scene")
        sceneElement.set("name", scene.getName())
        sceneElement.set("isProtag", str(scene.getIsProtag()))
        sceneSpriteLocElement = ET.SubElement(sceneElement, "sprite_loc")
        sceneSpriteLocElement.text = scene.getSpriteLoc()
        sceneSpriteNameElement = ET.SubElement(sceneElement, "sprite_name")
        sceneSpriteNameElement.text = scene.getSpriteName()
        sceneMusicLocElement = ET.SubElement(sceneElement, "music_loc")
        sceneMusicLocElement.text = scene.getMusicLoc()
        sceneMusicNameElement = ET.SubElement(sceneElement, "music_name")
        sceneMusicNameElement.text = scene.getSongName()
        sceneBackgroundLocElement = ET.SubElement(sceneElement, "background_loc")
        sceneBackgroundLocElement.text = scene.getBackgroundLoc()
        sceneTextSpokenElement = ET.SubElement(sceneElement, "text_spoken")
        sceneTextSpokenElement.text = scene.getTextSpoken()
        sceneTransitionElement = ET.SubElement(sceneElement, "transition")
        sceneTransitionElement.text = scene.getTransition()

    tree = ET.ElementTree(root)

    tree.write(file_name)


def load(file_name):
    global scenes
    global scenesOrdered

    scenes = {}
    scenesOrdered = []

    tree = ET.parse(file_name)
    root = tree.getroot()

    scenesElement = root.find("scenes")
    for newSceneElement in scenesElement:
        newSceneName = newSceneElement.get("name")
        newSceneIsProtagStr = newSceneElement.get("isProtag")
        if newSceneIsProtagStr == "True":
            newSceneIsProtag = True
        else:
            newSceneIsProtag = False
        newSceneSpriteLoc = newSceneElement.find("sprite_loc").text
        newSceneSpriteName = newSceneElement.find("sprite_name").text
        newSceneMusicLoc = newSceneElement.find("music_loc").text
        newSceneMusicName = newSceneElement.find("music_name").text
        newSceneBackgroundLoc = newSceneElement.find("background_loc").text
        newSceneTextSpoken = newSceneElement.find("text_spoken").text
        newSceneTransition = newSceneElement.find("transition").text

        finalScene = Scene.Scene(name=newSceneName, isProtag=newSceneIsProtag, spriteLoc=newSceneSpriteLoc,
                                 spriteName=newSceneSpriteName, musicLoc=newSceneMusicLoc, songName=newSceneMusicName,
                                 backgroundLoc=newSceneBackgroundLoc, textSpoken=newSceneTextSpoken,
                                 transition=newSceneTransition)

        scenesOrdered.append(finalScene)
        scenes[newSceneName] = finalScene

    updateSceneList()


# SCENE STUFF
scenes = {}
scenesOrdered = []

# UI STUFF
sceneButtons = [
    [sg.Button("Move Scene Up", key="SceneUp")],
    [sg.Button("Detete Scene", key="DeleteScene")],
    [sg.Button("Move Scene Down", key="SceneDown")]
]
sceneListBox = sg.Listbox(values=[], enable_events=True, size=(40, 6), key="SceneList")
newSceneUI = [
    [sg.Input(size=(32, 3), key="SceneNameText", do_not_clear=False)],
    [sg.Button("New Scene", key="NewScene"), sg.Button("Rename Current Scene", key="RenameScene")]
]
saveLoadText = sg.Text("", key="SaveLoadText", size=(60, 1))

filesText = [[sg.Text("Sprite File Location:")],
             [sg.Text("Music File Location:")],
             [sg.Text("Background File Location:")]]

filesSubstance = [
    [sg.Input(key="ImageFileInput", enable_events=True, disabled=True),
     sg.FileBrowse(disabled=True),
     sg.Button("Open", key="OpenSprite", disabled=True)],
    [sg.Input(key="MusicFileInput", enable_events=True, disabled=True),
     sg.FileBrowse(disabled=True),
     sg.Button("Open", key="OpenMusic", disabled=True)],
    [sg.Input(key="BackgroundFileInput", enable_events=True, disabled=True),
     sg.FileBrowse(disabled=True),
     sg.Button("Open", key="BackgroundMusic", disabled=True)]
]

transitions = [
    "Appear",
    "Fade",
    "Shift Left",
    "Shift Right",
    "Come From Bottom",
    "Come From Bottom w/ Shift Left",
    "Come From Bottom w/ Shift Right"
]

personNameInput = sg.Input(key="PersonName", enable_events=True, disabled=True)
songNameInput = sg.Input(key="SongName", enable_events=True, disabled=True)
protagTextBox = sg.Checkbox("Is the Person Talking the Protag?", key="IsProtagBox", disabled=True, enable_events=True)
textToSayInput = sg.Input(key="Saying", enable_events=True, disabled=True, size=(100, 400))
transitionSelect = sg.Listbox(values=transitions, enable_events=True, disabled=True, size=(40, 4), key="Transition")
transitionText = sg.Text("Current transition is:", size=(60, 1))

stuffToDisable = [
    personNameInput,
    songNameInput,
    protagTextBox,
    textToSayInput,
    transitionSelect
]

for arr in filesSubstance:
    for thing in arr:
        stuffToDisable.append(thing)

layout = [
    [sg.Text("Welcome to the Danganronpa Text Generator!", font=["Arial", 30])],
    [sg.Input(key="SaveFileInput"), sg.FileBrowse(), sg.Button("Save", key="Save"), sg.Button("Load", key="Load")],
    [saveLoadText],
    [sg.HorizontalSeparator()],
    [sg.Column([[sceneListBox]]), sg.Column(sceneButtons), sg.Column(newSceneUI)],
    [sg.HorizontalSeparator()],
    [sg.Text("Note: for all values, if it is the same as the last scene you can leave it blank!")],
    [sg.Column(filesText), sg.Column(filesSubstance)],
    [sg.Text("What is the name of the song?"),
     songNameInput],
    [sg.Text("What is the name of the person talking?"),
     personNameInput],
    [protagTextBox],
    [sg.Text("What are they saying?")],
    [textToSayInput],
    [sg.Text("Transition:")],
    [transitionSelect],
    [transitionText]
]

save_count = 0
load_count = 0

# Create the window
window = sg.Window("DR Text Generator Ver. 0.1", layout)

# Create an event loop
while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == "RenameScene" and values["SceneList"] != []:
        sceneName = values["SceneList"][0]
        toRename = scenes[sceneName]
        scenes.pop(sceneName)

        newName = values["SceneNameText"]
        toRename.rename(newName)
        scenes[newName] = toRename

        updateSceneList()

    if event == "NewScene":
        newName = values["SceneNameText"]
        newScene = Scene.Scene(newName)

        scenes[newName] = newScene
        scenesOrdered.append(newScene)
        updateSceneList()

    if event == "DeleteScene" and values["SceneList"] != []:
        sceneToDel = scenes.pop(values["SceneList"][0])
        scenesOrdered.remove(sceneToDel)

        updateSceneList()

    if event == "SceneUp" and values["SceneList"] != []:
        sceneMoved = scenes[values["SceneList"][0]]
        index = scenesOrdered.index(sceneMoved)

        if index - 1 < 0:
            continue

        scenesOrdered.pop(index)
        scenesOrdered.insert(index - 1, sceneMoved)

        updateSceneList()

    if event == "SceneDown" and values["SceneList"] != []:
        sceneMoved = scenes[values["SceneList"][0]]
        index = scenesOrdered.index(sceneMoved)

        if index + 1 > len(scenesOrdered):
            continue

        scenesOrdered.pop(index)
        scenesOrdered.insert(index + 1, sceneMoved)

        updateSceneList()

    if event == "Save":
        save_count += 1
        load_count = 0
        if save_count == 2 and values["SaveFileInput"] != "":
            saveLoadText.update("Saved!")
            save(values["SaveFileInput"])
        elif save_count == 2:
            saveLoadText.update("Invalid File Name!")
            save_count = 0
        else:
            saveLoadText.update("Are You Sure You Want To Save? (Press Save again to save)")
    elif event == "Load":
        load_count += 1
        save_count = 0
        if load_count == 2 and values["SaveFileInput"] != "":
            try:
                load(values["SaveFileInput"])
                print("finished loading")
                saveLoadText.update("Loaded!")
                load_count = 0
            except FileNotFoundError:
                saveLoadText.update("File Not Found!")
                load_count = 0
        elif load_count == 2:
            saveLoadText.update("Invalid File Name!")
            load_count = 0
        else:
            saveLoadText.update("Are You Sure You Want To Load? (Press Load again to load)")
    else:
        load_count = 0
        save_count = 0
        saveLoadText.update("")

    if event == "OpenMusic":
        try:
            os.startfile(values["MusicFileInput"])
        except (OSError, IOError) as e:
            print("Invalid File!!")
            continue

    if event == "ImageFileInput" and values["SceneList"] != []:
        scenes[values["SceneList"][0]].setSpriteLoc(values["ImageFileInput"])

    if event == "PersonName" and values["SceneList"] != []:
        scenes[values["SceneList"][0]].setSpriteName(values["PersonName"])

    if event == "SongName" and values["SceneList"] != []:
        scenes[values["SceneList"][0]].setSongName(values["SongName"])

    if event == "Saying" and values["SceneList"] != []:
        scenes[values["SceneList"][0]].setTextSpoken(values["Saying"])

    if event == "MusicFileInput" and values["SceneList"] != []:
        scenes[values["SceneList"][0]].setMusicLoc(values["MusicFileInput"])

    if event == "BackgroundFileInput" and values["SceneList"] != []:
        scenes[values["SceneList"][0]].setBackgroundLoc(values["BackgroundFileInput"])

    if event == "IsProtagBox" and values["SceneList"] != []:
        scenes[values["SceneList"][0]].setIsProtag(values["IsProtagBox"])

    if event == "Transition" and values["SceneList"] != []:
        scenes[values["SceneList"][0]].setTransition(values["Transition"][0])

    if not sceneListBox.get():
        for item in stuffToDisable:
            item.update(disabled=True)
            if item.Type == "input":
                item.update(value="")
            if item.Type == "checkbox":
                item.update(value=False)
        transitionText.update(value="Current transition is: ")

    else:
        sceneName = sceneListBox.get()[0]
        theScene = scenes[sceneName]
        for item in stuffToDisable:
            item.update(disabled=False)

            if item.Type != "button" and item.Type != "listbox":
                daValue = theScene.get(item.Key)
                if daValue is None:
                    daValue = ""
                item.update(value=daValue)
        tText = "Current transition is: " + theScene.getTransition()
        transitionText.update(value=tText)

window.close()
