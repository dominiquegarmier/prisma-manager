# prisma schema manage
do you have multiple enviroments that depend on the same prisma schema? perhaps even across multiple languages?
you can now use prisma schema manager to keep your schema in a central place and keep your dependant repositories up to date

## about

this tool was originally developed as an interal tool at [tostudyio](https://github.com/tostudyio) to manage prisma schemas across multiple dependant repositories.

## usage

Fork this repo, and write your own schema in the `database/prisma/models.schema`.
Now you can simply install your forked repo using pip and codegen your client in no time.

### install (npm)
coming soon ...

### install (pip)

```
pip install git+ssh://git@github.com/username/repo
```

### usage
```
db-cli -h
usage: db-cli [-h] {build,codegen} ...

build schema for desired client

positional arguments:
  {build,codegen}
    build          build schema
    codegen        codegen schema

options:
  -h, --help       show this help message and exit
```

#### build
```
db-cli build *language*
```

#### codegen
```
db-cli codegen
```

### development

#### build
```
cd database
python cli.py build *language*
```

#### migrate changes
when your schema changes you will have to migrate it to the database using the following commands.

##### using prisma migrate
use this in production to not lose any information

##### force push (development only)

***WARNING*** this will drop everything
```
cd database
npx prisma migrate reset
npx prisma db push
```

## license
[MIT](./LICENSE)


## planned features
support other prisma clients such as `prisma-client-rust`, `prisma-client-go`, with that would come support for other package managers such as `npm`, `yarn`, `cargo`, `go get`

## currently supported
- `prisma-client-py`
- `prisma-client-js`