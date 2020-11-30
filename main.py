import importlib.util

for x in [1, 2, 1, 2]:
    spec = importlib.util.spec_from_file_location("run", "mod{0}/mod{0}.py".format(x))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module.run({"name": "Paulo {0}".format(x)})
