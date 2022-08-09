from beets.plugins import BeetsPlugin
from beets.ui import Subcommand

my_super_command = Subcommand('super', help='do something super')
def say_hi(lib, opts, args):
    print("Hello everybody! I'm customtags plugin!")
my_super_command.func = say_hi

#class SuperPlug(BeetsPlugin):
#    def commands(self):
#       return [my_super_command]

class CustomTags(BeetsPlugin):
  def __init__(self):
    super(CustomTags, self).__init__()
    #self.register_listener('pluginload', self.loaded)
    self._log.info('first Plugin loaded!')
    #return [my_super_command]
