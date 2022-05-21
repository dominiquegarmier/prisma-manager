# prisma-manager
This is a template repository to manage prisma schemas for multiple clients. It makes your schemas installable with `pip`. When installing a prisma-manager repo you will also get access to a cli to switch between clients and run codgen.

## about

this tool was originally developed as an interal tool at [tostudyio](https://github.com/tostudyio) to manage prisma schemas across multiple dependant repositories.

## usage

Create a repo using this template and customize the schemas located at `database/prisma/`.

- create `schema.prisma` like you would in any prisma project
- create `*client*.prisma` for any client you would like to support, this file should only contain the generator block.

If you are confused take a look at the default files [`database/prisma/`](./database/prisma/).

If you are using other clients the `prisma-client-py` you should add those additional dependencies to `setup.py` or `setup.cfg` or install them manually.

### install
if you used `prisma-manager` as your repo template you should be able to install it directly with pip
```
pip install git+ssh://git@github.com/username/your-templated-repo
```
you can also just try it out directly by installing the template
```
pip install git+ssh://git@github.com/dominiquegarmier/prisma-manager
```

if there is intrest there might come support for other packaging tools such as `npm`, `go-get`, `cargo`

### cli
Once you have installed your templated repo you will have access the the `prisma-manager` cli.

#### codegen
generate the specified client
```
prisma-manager codgen *client*
```
with python:
```
prisma-manager codgen python
```
you can now import the client in python
```python
from prisma import Prisma
```

## FAQ

#### why not make a meta package
By meta package I mean primarily a tool (like [`pre-commit`](https://github.com/pre-commit/pre-commit)) which allows you to create packages.

A:
This would probably be the best way to go about this whole thing. However it's alot of added complexity which I dont see as necessary right now. As the project grows more complex this might become necessary.


## license
[MIT](./LICENSE)
