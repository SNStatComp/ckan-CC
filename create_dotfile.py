import sys

def read_input (filename):
	f=open (filename,'r')
	image2dir={}
	dir2image={}
	for line in f.readlines():
		args=line.split(':FROM')
		if len(args)!=2:
			continue
		dirname=args[0].strip().replace('Dockerfile','')
		dockerimage=args[1].strip()
		dir2image[dirname]=dockerimage
		image2dir[dockerimage]=dirname
	return dir2image, image2dir

def read_output (filename):
	f=open (filename,'r')
	image2dir={}
	dir2image={}
	for line in f.readlines():
		args=line.split('-t ')
		if len(args)!=2:
			continue
		dirname=args[0].split(':')[0].replace('build','').strip()
		dockerimage=args[1].replace(' .','').strip()
		dir2image[dirname]=dockerimage
		image2dir[dockerimage]=dirname
	return dir2image, image2dir


images_in, dir_in=read_input (sys.argv[1])
images_out,dir_out=read_output (sys.argv[2])

for k,v in images_in.items():
	print k,v
print
print '**'
for k,v in dir_in.items():
	print k,v

print '---'

f=open (sys.argv[3],'w')
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
