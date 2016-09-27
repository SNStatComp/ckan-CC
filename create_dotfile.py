import sys, subprocess

def read_input (txt):
	image2dir={}
	dir2image={}
	for line in txt:
		args=line.split(':FROM')
		if len(args)!=2:
			continue
		dirname=args[0].strip().replace('Dockerfile','')
		dockerimage=args[1].strip()
		dir2image[dirname]=dockerimage
		image2dir[dockerimage]=dirname
	return dir2image, image2dir

def read_output (txt):
	image2dir={}
	dir2image={}
	for line in txt:
		args=line.split('-t ')
		if len(args)!=2:
			continue
		dirname=args[0].split(':')[0].replace('build','').strip()
		dockerimage=args[1].replace(' .','').strip()
		dir2image[dirname]=dockerimage
		image2dir[dockerimage]=dirname
	return dir2image, image2dir


raw_images_in = subprocess.check_output('grep -r -i --include Dockerfile From', shell=True)
raw_images_out = subprocess.check_output('grep -r -i --include build docker', shell=True)


images_in, dir_in=read_input (raw_images_in)
images_out,dir_out=read_output (raw_images_out)

for k,v in images_in.items():
	print k,v
print
print '**'
for k,v in dir_in.items():
	print k,v

print '---'


outfile='buildstruct'
f=open (outfile,'w')
f.write('digraph buildstruct {\n')
for dirname, image in images_in.items():

	if image in dir_in:
#		print image, dir_inimage]
		if dir_in[image] in images_out:
			s=image.replace('-','_') + '->' + images_out[dir_in[image]].replace('-','_')
			print  s
			s=s.replace('/','_')
			f.write(s+';\n')
f.write('}\n')
f.close()

os.system ('dot -Tpng buildstructure -o buildstructure.png')

