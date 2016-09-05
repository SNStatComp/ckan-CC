from ckanapi import LocalCKAN, ValidationError

registry = LocalCKAN(user='alex')
registry.action.package_create(name='testdata', title='this will work fine')
