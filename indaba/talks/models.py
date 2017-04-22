from django.db import models
from markitup.fields import MarkupField
from django.core.urlresolvers import reverse
from django.conf import settings


class Talk_Type(models.Model):

    talk_types = (
        ('S', "Short_Talk"),
        ('L', "Long_Talk"),
         ('T', "Tutorial"),
    )

    name = models.CharField(choices=talk_types, max_length=1)

    def __str__(self):
        return u"%s" % (self.name)


class Proposal(models.Model):

    # proposal = models.CharField(max_length=255, blank=False)
    title = models.CharField(max_length=1024)
    description = models.TextField(
        ("Brief Description"),
        max_length=400,  blank=True, # @@@ need to enforce 400 in UI
        help_text=("If your proposal is accepted this will be made public"
        " and printed in the "
        "program. Should be one paragraph, maximum 400 characters.")
    )
    abstract = models.TextField(
        ("Detailed Abstract"),
        help_text=("Detailed outline. Will be made public if your proposal is accepted. Edit "
                    "using <a href='http://daringfireball.net/projects/markdown/basics' "
                    "target='_blank'>Markdown</a>.")
    )
    talk_type = models.ForeignKey(Talk_Type)
    proposal_id = models.AutoField(primary_key=True, default=None)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="proposals", default='')
    additional_notes = models.TextField(
        ("Addtional Notes"),
        blank=True,
        help_text=("Anything else you'd like the program committee to know when making their "
                    "selection: your past experience, etc. This is not made public. Edit using "
                    "<a href='http://daringfireball.net/projects/markdown/basics' "
                    "target='_blank'>Markdown</a>.")
    )
    # meetup = models.ForeignKey()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("home")
