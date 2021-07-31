using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class FadeOut : MonoBehaviour
{
    public bool isFadingOut;
    public float timeLeft;

    // Update is called once per frame
    void Update()
    {
        if (isFadingOut)
        {
            timeLeft -= Time.deltaTime;
            GetComponent<SpriteRenderer>().color = new Color(1, 1, 1, 2*timeLeft);

            if (timeLeft < 0)
            {
                Destroy(gameObject);
            }
        }
    }

    public void fadeOut()
    {
        timeLeft = 0.5f;
        isFadingOut = true;
    }

}
