from django.db.models import Model, TextField, DateTimeField, CharField, ForeignKey, FloatField

class Tweet(Model):
    text = TextField()
    created_at = DateTimeField()
    id_str = CharField(unique = True, max_length = 20)
    profile_image_url = CharField(max_length = 200)
    from_user = CharField(max_length = 50)
    lat = FloatField(blank=True, null=True)
    long = FloatField(blank=True, null=True)

    def __unicode__(self):
        return '%s: %s' % (self.from_user, self.text)

    class Meta:
        ordering = ['created_at']

class Photo(Model):
    name = CharField(unique = True, max_length = 200, blank = True, null = True)
    tweet = ForeignKey(Tweet, related_name = 'photos')
    
    def __unicode__(self):
        return '%s: %s' % (self.tweet.text, self.name)
