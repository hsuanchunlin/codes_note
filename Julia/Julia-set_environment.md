# Study note for julia - Set the environment
## Create an environment

- Use "]" to enter package management mode in Julia
- Use [delete] to return 
- Use "?" to search the commands. e.g. ?download
- "@" expands to
	1. an active project (activated with Pkg.activate/pkg> activate) or 
	1. the home project. We can check the expanded load path with Base.load_path()

## Autimatic activate julia project
```julia
using Pkg
if isfile("Project.toml") && isfile("Manifest.toml")
    Pkg.activate(".")
end
```

## Create a julia environment
- Generate a project environment, just simply enter the pkg mode by pressing "]" then type *generate* follow by environment/project name.

```julia
generate myenvironment
```
- Activate the project
```julia
activate myenvironment
```
or
```julia
activate .
```

## Add or update packages

- Under package management mode (enter by pressing "]")

```julia
add packagename
```
for example
```
add CSV
```

## Check environment status

```
status
```

## For using Pkg under julia console

```
using Pkg
Pkg.status()
```

another way to activate the environment is 

```
using Pkg
Pkg.activate(".")
```
