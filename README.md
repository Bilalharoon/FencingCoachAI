A model to recognize different fencing actions

* Download the videos off youtube
* Train the model to recognize fencing actions
* return statistics and advice


```
video = process_video(url)
fencing_actions = Parsjson(url)
# handsnipe, lunge, thrust, advance, retreat, zornhau, ablouffen
model = train_model(video, fencing_actions)

new_video = process_video("video.mp4")
model.analyze(new_video)

```

annotation_structure

```json
{
    "video_id": "fencing1.mp4",
    "frames": [
        {
            "timestamp": "0:12",
            "fotl": {
                "action": "lunge",
                "vor": true
                },
            "fotr":{
                "action": "parry"
                "vor": false
            }

        } 
    ]
}

```