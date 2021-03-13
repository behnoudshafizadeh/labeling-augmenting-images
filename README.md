# labeling and augmenting-images

## DISCRIPTION
> in this project,we follow the process of labeling license-plate image dataset by helping [makesense](https://www.makesense.ai/) online website,beside,by using [imgaug](https://github.com/aleju/imgaug) and [automold](https://github.com/UjjwalSaxena/Automold--Road-Augmentation-Library),we enable to augment our dataset in five different conditions `fogy,rainy,snowy,brighten,darken`,so by increasing dataset we will provide better learning of object detection algorithm in different conditions and by labling them using them for training procedure of object detection task.

## labeling phase 
> go to [makesense](https://www.makesense.ai/) website and see optional useage of this website in different task in computer vision specially in object detection task,in this site,only by using mouse we enable to label our image,per image we have on label text with `.txt` or `.xml`,both of them used for object detection task,but we used `.txt` file for training algorithm.in below you see the example of labeling dataset:

 |    image | label |
 | -------- | ----- | 
 | ![sample image](https://user-images.githubusercontent.com/53394692/111023833-7730ab00-83f0-11eb-8ed0-13b11b251e1f.PNG) | ![sample label](https://user-images.githubusercontent.com/53394692/111023846-8e6f9880-83f0-11eb-899c-04f092ceefea.PNG) | 

## augmenting phase
> for augmenting images,put `brighten-augment.py` and `darken-augment.py` in `Automold--Road-Augmentation-Library-master` directory,furthermor,put `foggy-augment.py`,`snowy-augment.py`and `rainy-augment.py` in `imgaug-master` directory,because packages in these codes are related to these `repos`.after that run the following codes.

> HINT : change `directory` as `main_path` variable basis on your `PATH` in your system,furthermore you can able to change intensity of (snow,fog,darkness,...) with refering to the refrence sites of [imgaug](https://github.com/aleju/imgaug) and [automold](https://github.com/UjjwalSaxena/Automold--Road-Augmentation-Library).


## Applying Augmentation 
> run below `.py` files  in your terminal:
```
for applying rain in iamges:
python rainy-augment.py

for applying snow in images:
python snowy-augment.py

for applying fog in images :
python foggy-augment.py

for applying brightness in images :
python brighten-augment.py

for applying darkness in images :
python darken-augment.py

```
> after running codes,you can see reuslts as below:

|             | augmented-dataset | 
| ----------- | -------- | 
|   rainy  | ![rainy](https://user-images.githubusercontent.com/53394692/111022475-36349880-83e8-11eb-919f-49f1b4150df2.PNG) | 
|  foggy   | ![foggy](https://user-images.githubusercontent.com/53394692/111022483-3d5ba680-83e8-11eb-9a63-f39f12c16340.PNG) | 
| snowy    | ![snowy](https://user-images.githubusercontent.com/53394692/111022470-316fe480-83e8-11eb-8de8-1fcbd6e1ed09.PNG) | 
| brighten |  ![brighten](https://user-images.githubusercontent.com/53394692/111022480-39c81f80-83e8-11eb-99f1-ef24855d60a6.PNG) | 
|  darken  | ![darken](https://user-images.githubusercontent.com/53394692/111022477-3896f280-83e8-11eb-932d-7b4011c2859b.PNG)  | 


## LICENSE
> this project was done by me `behnoud shafizadeh` and my co-worker `navid pourhadi` in the kharazmi university lab,supervised by `DR.Farshad Eshghi` and `DR.Manoochehr KelarEstaghi`,so the full source of code and dataset in this project are out authority and related to `kharazmi university of tehran`,so if you would like to contiribute with our group and access to out document,please contact with our emails : `behnud.shafizadeh@gmail.com` and `npourhadi1998@gmail.com`,thanks for your consideration.


