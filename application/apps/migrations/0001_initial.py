# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Applicant'
        db.create_table(u'apps_applicant', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('lastname', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('firstname', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('essay', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal(u'apps', ['Applicant'])

        # Adding model 'Recommender'
        db.create_table(u'apps_recommender', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('applicant', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['apps.Applicant'])),
            ('lastname', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('firstname', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('letter', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal(u'apps', ['Recommender'])


    def backwards(self, orm):
        # Deleting model 'Applicant'
        db.delete_table(u'apps_applicant')

        # Deleting model 'Recommender'
        db.delete_table(u'apps_recommender')


    models = {
        u'apps.applicant': {
            'Meta': {'object_name': 'Applicant'},
            'email': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'essay': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'firstname': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastname': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'apps.recommender': {
            'Meta': {'object_name': 'Recommender'},
            'applicant': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['apps.Applicant']"}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'firstname': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastname': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'letter': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['apps']