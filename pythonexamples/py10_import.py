print('"Normal import"')
import module
module.test()
# main module

print('\n"Submodule import"')
import module.other_module
module.other_module.test()
# submodule call

print('\n"Import from"')
from module import test
test()
# main module

print('\n"Import from as"')
from module.other_module import test as other_test
other_test()
# submodule call
