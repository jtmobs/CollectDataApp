from django.contrib.sessions.models import Session
from django.db import models
from html_matcher import MatchingSubsequences, MatchingSubsequencesOptimized, AllPathTreeEditDistance, \
    AllPathTreeEditDistanceOptimized
from rest_framework import serializers


class WebSite(models.Model):
    name = models.CharField(max_length=100, primary_key=True)


class Domain(models.Model):
    webSite = models.ForeignKey(WebSite, on_delete=models.CASCADE, to_field='name')
    domain = models.URLField(unique=True)


class WebPage(models.Model):
    webSite = models.ForeignKey(WebSite, on_delete=models.CASCADE, to_field='name')
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    url = models.URLField(max_length=1024, blank=True, null=True)
    eventType = models.CharField(max_length=100, blank=True, null=True)
    pageStructure = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    timeStamp = models.FloatField(blank=True, null=True)
    tag = models.CharField(max_length=50)
    targetId = models.CharField(max_length=1000, blank=True, null=True)
    classes = models.CharField(max_length=1000, blank=True, null=True)
    xpath = models.TextField()
    fullXpath = models.TextField()
    cssPath = models.TextField()
    sessionId = models.TextField()
    textContent = models.TextField(null=True, blank=True)
    mouseX = models.IntegerField(null=True, blank=True)  # Optional fields for mouse events
    mouseY = models.IntegerField(null=True, blank=True)
    key = models.CharField(max_length=50, blank=True, null=True)  # Optional field for key events


class WebPageIdentifier(models.Model):
    class SimilarityMethods(models.TextChoices):
        LCS = '1', 'MS'
        APTED = '2', 'APTED'
        LCS_OPTIMIZED = '3', 'MS_Optimized'
        APTED_OPTIMIZED = '4', 'APTED_Optimized'

    webPages = models.ManyToManyField(WebPage, through='WebPageIdentifierWebPage')
    url = models.URLField(max_length=1024)
    pageStructure = models.TextField()
    similarityMethod = models.CharField(max_length=2, choices=SimilarityMethods.choices,
                                        default=SimilarityMethods.LCS_OPTIMIZED)

    def get_similarity_method(self):
        if self.similarityMethod == '1':
            return MatchingSubsequences()
        elif self.similarityMethod == '2':
            return AllPathTreeEditDistance()
        elif self.similarityMethod == '3':
            return MatchingSubsequencesOptimized()
        elif self.similarityMethod == '4':
            return AllPathTreeEditDistanceOptimized()
        else:
            raise serializers.ValidationError("Similarity method does not exist")


class WebPageIdentifierWebPage(models.Model):
    webPage = models.ForeignKey(WebPage, on_delete=models.CASCADE)
    webPageIdentifier = models.ForeignKey(WebPageIdentifier, on_delete=models.CASCADE)
    similarity = models.DecimalField(decimal_places=2, max_digits=3)
    created_at = models.DateTimeField(auto_now_add=True)


class Sequence(models.Model):
    webPageIdentifiers = models.ManyToManyField(WebPageIdentifier, through='SequenceIdentifier')
    support = models.IntegerField(blank=True, null=True)


class SequenceIdentifier(models.Model):
    sequence = models.ForeignKey(Sequence, on_delete=models.CASCADE)
    webPageIdentifier = models.ForeignKey(WebPageIdentifier, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
