class Scene:

    def __init__(self, name, spriteLoc="",
                 musicLoc="", backgroundLoc="", spriteName="",
                 songName="", textSpoken="", isProtag=False,
                 transition="Appear"):
        self.name = name
        self.transition = transition
        self.spriteLoc = spriteLoc
        self.musicLoc = musicLoc
        self.backgroundLoc = backgroundLoc
        self.spriteName = spriteName
        self.isProtag = isProtag
        self.songName = songName
        self.textSpoken = textSpoken

    def getName(self):
        return self.name

    def rename(self, name):
        self.name = name

    def setTransition(self, tran):
        self.transition = tran

    def setSpriteLoc(self, loc):
        self.spriteLoc = loc

    def setMusicLoc(self, loc):
        self.musicLoc = loc

    def getMusicLoc(self):
        return self.musicLoc

    def getSpriteLoc(self):
        return self.spriteLoc

    def getTransition(self):
        return self.transition

    def getBackgroundLoc(self):
        return self.backgroundLoc

    def setBackgroundLoc(self, loc):
        self.backgroundLoc = loc

    def setSpriteName(self, name):
        self.spriteName = name

    def getSpriteName(self):
        return self.spriteName

    def setIsProtag(self, isProtag):
        self.isProtag = isProtag

    def getIsProtag(self):
        return self.isProtag

    def getSongName(self):
        return self.songName

    def setSongName(self, name):
        self.songName = name

    def getTextSpoken(self):
        return self.textSpoken

    def setTextSpoken(self, msg):
        self.textSpoken = msg

    def get(self, key):
        if key == "PersonName":
            return self.spriteName
        if key == "SongName":
            return self.songName
        if key == "IsProtagBox":
            return self.isProtag
        if key == "Saying":
            return self.textSpoken
        if key == "ImageFileInput":
            return self.spriteLoc
        if key == "MusicFileInput":
            return self.musicLoc
        if key == "BackgroundFileInput":
            return self.backgroundLoc

        return "aaaaaaaaaaaaaaaaaaaaaaaaaa"
