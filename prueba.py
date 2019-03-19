import subprocess


Numero = ['1','2']

for n in Numero:
	subprocess.call( 'python yolo.py --image images/imagen'+ n +'.jpg --yolo yolo-coco',shell = True)


	