from mechanize import Browser
import re


def select_control(control):
  r = re.compile(r'IgnoreControl')
  return bool(re.match(r, control.name))


url = 'https://moversguide.usps.com/icoa/move-info/icoa-main-flow.do?execution=e1s8&_flowId=icoa-main-flow'
br = Browser()
br.set_handle_robots(False)
br.open(url)
for form in br.forms():
    print "Form name:", form.name
    print form
br.form = list(br.forms())[0]
print br.form

br.form.set_all_readonly(False)
for control in br.form.controls:
    print control
    #print "type=%s, name=%s value=%s" % (control.type, control.name, br[control.name])

# ctl = br.form.find_control(predicate=select_control)
# ctl.value = '_eventId_continue'

# br.form['_eventId_continue'] = 'continue'
br.submit()
a = br.response()
br.select_form("forwadingPeriod")

for form in br.forms():
    print "2 Form name:", form.name
    print form

for control in br.form.controls:
    print control

br.form.set_all_readonly(False)
# ctl = br.form.find_control(predicate=select_control)
# ctl.value = 'continue'
br.form['isPermanent'] = ['true',]
br.form['startDateStr']='5/30/2017'
br.form['endDateStr']='5/30/2017'
br.form['type'] = ['INDIVIDUAL',]
br.form['_eventId_back'] = ''
ctrl = br.form.find_control('_eventId_back')
ctrl.disabled = True

#br.form['_eventId_continue'] = 'continue'
# ctl = br.form.find_control(name='_eventId_continue', nr=0)
# ctl.value = 'continue'
#br.submit(name='Continue',nr=0)
#br.click(name='Continue',nr=0)
br.submit()
for form in br.forms():
    print "Form name:", form.name
    print form

# for control in br.form.controls:
#     print control

# a = br.response()
# print a.read()
