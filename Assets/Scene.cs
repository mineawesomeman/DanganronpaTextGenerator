using System.Collections;
using System.Collections.Generic;
using System.IO;
using UnityEngine;

public class Scene
{
    private string name;
    private string spriteLoc;
    private string characterName;
    private string musicLoc;
    private string songName;
    private string backgroundLoc;
    private string textSpoken;
    private string transition;
    private bool isProtag;
    private Sprite sprite;
    private Texture2D scene;

    public Scene(string name, string spriteLoc = "", string characterName = "", string musicLoc = "", string songName = "", string backgroundLoc = "", string textSpoken = "", string transition = "", bool isProtag = false)
    {
        this.name = name;
        this.spriteLoc = spriteLoc;
        this.characterName = characterName;
        this.musicLoc = musicLoc;
        this.songName = songName;
        this.backgroundLoc = backgroundLoc;
        this.textSpoken = textSpoken;
        this.transition = transition;
        this.isProtag = isProtag;
        
        if (!spriteLoc.Equals(""))
            sprite = getSpriteFromImagePath(spriteLoc);

        if (!backgroundLoc.Equals(""))
            scene = getTextureFromImagePath(backgroundLoc);
    }

    
    private Sprite getSpriteFromImagePath(string imagePath)
    {
        Texture2D texture = getTextureFromImagePath(imagePath);
        Sprite ret = Sprite.Create(texture, Rect.MinMaxRect(0, 0, texture.width, texture.height), new Vector2(0, 0));
        return ret;
    }
    private Texture2D getTextureFromImagePath(string imagePath)
    {
        Texture2D texture = new Texture2D(2, 2);
        byte[] img = imageToByteArray(imagePath);
        texture.LoadImage(img);
        return texture;
    }
    private byte[] imageToByteArray(string imagePath)
    {
        byte[] imageByteArray = null;
        FileStream fileStream = new FileStream(imagePath, FileMode.Open, FileAccess.Read);
        using (BinaryReader reader = new BinaryReader(fileStream))
        {
            imageByteArray = new byte[reader.BaseStream.Length];
            for (int i = 0; i < reader.BaseStream.Length; i++)
                imageByteArray[i] = reader.ReadByte();
        }
        return imageByteArray;
    }

    public string toString()
    {
        string str = "";

        str += "name :" + name + "\n";
        str += "sprite: " + characterName + "\n";
        str += "music: " + songName + "\n";

        return str;
    }

    public string getName() { return name; }
    public string getSpriteLoc() { return spriteLoc; }
    public string getCharacterName() { return characterName; }
    public string getMusicLoc() { return musicLoc; }
    public string getSongName() { return songName; }
    public string getBackgroundLoc() { return backgroundLoc; }
    public string getTextSpoken() { return textSpoken; }
    public string getTransition() { return transition; }
    public bool getIsProtag() { return isProtag; }
    public Sprite getSprite() { return sprite; }
    public Texture2D getScene() { return scene; }
}
