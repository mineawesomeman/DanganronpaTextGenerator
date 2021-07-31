using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class NameBehavior : MonoBehaviour
{
    public float state;
    public string charName;
    public float speed;

    // Start is called before the first frame update
    void Start()
    {
        state = 0;
    }

    // Update is called once per frame
    void Update()
    {
        

        if (state != 0)
        {
            if (state <= 20)
            {
                GetComponent<RectTransform>().anchoredPosition = new Vector2 (-597f, -60f + state);

                GetComponent<Text>().color = new Color(0.1882353f, 0.2039216f, 0.2078431f, (20f - state) / 20f);

                state += Time.deltaTime * speed;
            } else if (state <= 40)
            {
                GetComponent<Text>().text = charName;
                GetComponent<RectTransform>().anchoredPosition = new Vector2 (-597f, -60f + (40 - state));

                GetComponent<Text>().color = new Color(0.1882353f, 0.2039216f, 0.2078431f, (state - 20f) / 20f);

                state += Time.deltaTime * speed;
            } else
            {
                state = 0f;
            }
        } else
        {
            GetComponent<RectTransform>().anchoredPosition = new Vector2(-597f, -60f);

            GetComponent<Text>().color = new Color(0.1882353f, 0.2039216f, 0.2078431f);
        }
    }

    public void newName(string n)
    {
        charName = n;
        state = .1f;
    }

    private IEnumerator newNameAnimation()
    {
        while (true)
        {
            while (Vector3.Distance(transform.position, new Vector3(-597f, -40f, 0f)) > 1f)
            {

            }
        }
    }
}
