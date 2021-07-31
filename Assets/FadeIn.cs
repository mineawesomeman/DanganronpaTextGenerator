using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class FadeIn : MonoBehaviour
{
    public bool isFadingIn;
    public float fadeIn;

    // Update is called once per frame
    void Update()
    {
        if (isFadingIn)
        {
            fadeIn += Time.deltaTime;
            GetComponent<SpriteRenderer>().color = new Color(1, 1, 1, fadeIn*2);
            
            if (fadeIn > 0.5f)
            {
                isFadingIn = false;
            }
        }
    }
}
