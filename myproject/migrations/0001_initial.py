# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'User'
        db.create_table(u'myproject_user', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('pv_id', self.gf('django.db.models.fields.IntegerField')()),
            ('tag_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('short_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'myproject', ['User'])

        # Adding model 'Review'
        db.create_table(u'myproject_review', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_timestamp', self.gf('django.db.models.fields.BigIntegerField')()),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['myproject.User'])),
            ('review_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='assigned_reviews', to=orm['myproject.User'])),
            ('pv_link', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('project_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('github_link', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('story_type', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('story_id', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'myproject', ['Review'])


    def backwards(self, orm):
        # Deleting model 'User'
        db.delete_table(u'myproject_user')

        # Deleting model 'Review'
        db.delete_table(u'myproject_review')


    models = {
        u'myproject.review': {
            'Meta': {'object_name': 'Review'},
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['myproject.User']"}),
            'created_timestamp': ('django.db.models.fields.BigIntegerField', [], {}),
            'github_link': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'pv_link': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'review_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'assigned_reviews'", 'to': u"orm['myproject.User']"}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'story_id': ('django.db.models.fields.IntegerField', [], {}),
            'story_type': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'myproject.user': {
            'Meta': {'object_name': 'User'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'pv_id': ('django.db.models.fields.IntegerField', [], {}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'tag_name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['myproject']