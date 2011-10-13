from django.db import models
from django.utils.translation import ugettext_lazy as _

TSHIRT_CHOICES = (
    ('XS',_('XS')),
    ('S',_('S')),
    ('M',_('M')),
    ('L',_('L')),
    ('XL',_('XL')),
)

# Create your models here.
class BarcampRegistration(models.Model):
    """
    - name (required)
    - e-mail (required)
    - twitter
    - website
    - what size of t-shirt (xs s m l xl) (sizes similar to barcamp 4 tshirt (us size))
    - topics
    """
    name = models.CharField(_('name'),max_length=512)
    email = models.EmailField(_('e-mail'),
                                help_text=_('we will use this to contact you, and not display anywhere'))
    twitter = models.CharField(_('twitter'),max_length=512,blank=True,null=True,
                               help_text=_('twitter username without @'))
    website = models.URLField(_('website'),verify_exists=False,blank=True,null=True)
    tshirt_size = models.CharField(_('t-shirt size'),choices=TSHIRT_CHOICES,max_length=3,
                                   blank=True,null=True,help_text=_('US sizes'))
    topics = models.CharField(_('topics'),max_length=1024,blank=True,null=True)

    class Meta:
        unique_together = (('name','email'),)

    def __unicode__(self):
        return u'Barcamp Registration for: %s (%s)' % (self.name,self.email)