using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class Roation : MonoBehaviour
{

    public float timer;
    public float speed;
    RectTransform trs;

    // Start is called before the first frame update
    void Start()
    {
        trs = GetComponent<RectTransform>();
        timer = 0;
    }

    // Update is called once per frame
    void Update()
    {
        timer += Time.deltaTime;

        if (timer > 1f)
        {
            timer -= 1;
        }
        if (timer > (5f / 6))
        {
            trs.Rotate(new Vector3(0, 0, 1) * speed * Time.deltaTime);
        } else if (timer > (4f / 6))
        {
            trs.Rotate(new Vector3(0, 0, -2) * speed * Time.deltaTime);
        }
    }
}
