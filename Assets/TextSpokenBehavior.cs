using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class TextSpokenBehavior : MonoBehaviour
{
    public bool isFinishedTyping;
    public string text;
    public int textSpeed;
    float loc;

    // Start is called before the first frame update
    void Start()
    {
        loc = 0;
    }

    // Update is called once per frame
    void Update()
    {
        if (!isFinishedTyping)
        {
            loc += Time.deltaTime * textSpeed;
            GetComponent<Text>().text = text.Substring(0, Mathf.FloorToInt(loc));
        } else
        {
            GetComponent<Text>().text = text;
            loc = text.Length;
        }

        if (loc >= text.Length)
        {
            isFinishedTyping = true;
        }
    }

    public void newText(string s)
    {
        text = s;
        isFinishedTyping = false;
        loc = 0f;
    }
}
