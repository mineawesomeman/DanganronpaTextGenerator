using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.Xml;
using UnityEngine.UI;

public class SceneHolder : MonoBehaviour
{
    public List<Scene> scenes;
    public int currentScene;
    public int sceneCount;
    public GameObject textObject;
    public GameObject nameObject;
    public GameObject cameraObject;
    public GameObject appearSpritePrefab;
    public GameObject fadeSpritePrefab;
    public GameObject moveUpSpritePrefab;
    GameObject currentSprite;

    // Start is called before the first frame update
    void Start()
    {
        Debug.Log("haha");

        scenes = new List<Scene>();
        scenes.Add(new Scene("GENERATED_SCENE"));
        currentScene = 0;

        var reader = XmlReader.Create("input.xml");

        reader.ReadToFollowing("scenes");
        reader.MoveToAttribute("count");

        string sceneCountStr = reader.ReadContentAsString();
        sceneCount = int.Parse(sceneCountStr);

        for (int i = 0; i < sceneCount; i ++)
        {
            reader.ReadToFollowing("scene");

            reader.MoveToAttribute("name");
            string sceneName = reader.ReadContentAsString();

            reader.MoveToAttribute("isProtag");
            bool sceneIsProtag = reader.ReadContentAsString().Equals("True");

            reader.ReadToFollowing("sprite_loc");
            string sceneSpriteLoc = reader.ReadElementContentAsString();

            //reader.ReadToNextSibling(sceneName);
            string sceneSpriteName = reader.ReadElementContentAsString();

            //reader.ReadToFollowing("music_loc");
            string sceneMusicLoc = reader.ReadElementContentAsString();

            //reader.ReadToFollowing("music_name");
            string sceneMusicName = reader.ReadElementContentAsString();

            //reader.ReadToFollowing("background_loc");
            string sceneBackgroundLoc = reader.ReadElementContentAsString();

            string sceneTextSpoken = reader.ReadElementContentAsString();

            string sceneTransition = reader.ReadElementContentAsString();

            Scene scene = new Scene(sceneName, sceneSpriteLoc, sceneSpriteName, sceneMusicLoc, sceneMusicName, sceneBackgroundLoc, sceneTextSpoken, sceneTransition, sceneIsProtag);
            scenes.Add(scene);

            Debug.Log(scene.toString());
        }
    }                                       

    // Update is called once per frame
    void Update()
    {
        if (Input.GetMouseButtonDown(0))
        {
            if (!textObject.GetComponent<TextSpokenBehavior>().isFinishedTyping)
            {
                textObject.GetComponent<TextSpokenBehavior>().isFinishedTyping = true;
            }
            else if (currentScene < sceneCount)
            {
                currentScene++;
                //TODO make it not break on sceneoverflow

                textObject.GetComponent<TextSpokenBehavior>().newText(scenes[currentScene].getTextSpoken());

                string newName = scenes[currentScene].getCharacterName();

                if (!newName.Equals(""))
                {
                    nameObject.GetComponent<NameBehavior>().newName(newName);
                }

                string newSpriteLoc = scenes[currentScene].getSpriteLoc();

                if (!newSpriteLoc.Equals(""))
                {
                    GameObject oldSprite = currentSprite;
                    switch (scenes[currentScene].getTransition())
                    {
                        case "Fade":
                            currentSprite = Instantiate(fadeSpritePrefab);
                            currentSprite.GetComponent<SpriteRenderer>().sprite = scenes[currentScene].getSprite();
                            
                            if (oldSprite != null)
                            {
                                oldSprite.GetComponent<FadeOut>().fadeOut();
                            }
                            break;
                        default:
                            currentSprite = Instantiate(appearSpritePrefab);
                            currentSprite.GetComponent<SpriteRenderer>().sprite = scenes[currentScene].getSprite();
                            Destroy(oldSprite);
                            break;
                    }
                    
                    
                    
                    
                }
            }
        }
    }
}
