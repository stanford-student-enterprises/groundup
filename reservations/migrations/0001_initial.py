# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ReservationItem'
        db.create_table('reservations_reservationitem', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('price', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=6, decimal_places=2, blank=True)),
        ))
        db.send_create_signal('reservations', ['ReservationItem'])

        # Adding model 'Reservation'
        db.create_table('reservations_reservation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reservations.ReservationItem'])),
            ('quantity', self.gf('django.db.models.fields.IntegerField')()),
            ('pickup_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('reservations', ['Reservation'])

        # Adding model 'ReservationNotificationEmail'
        db.create_table('reservations_reservationnotificationemail', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('reservations', ['ReservationNotificationEmail'])


    def backwards(self, orm):
        # Deleting model 'ReservationItem'
        db.delete_table('reservations_reservationitem')

        # Deleting model 'Reservation'
        db.delete_table('reservations_reservation')

        # Deleting model 'ReservationNotificationEmail'
        db.delete_table('reservations_reservationnotificationemail')


    models = {
        'reservations.reservation': {
            'Meta': {'object_name': 'Reservation'},
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['reservations.ReservationItem']"}),
            'pickup_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'quantity': ('django.db.models.fields.IntegerField', [], {})
        },
        'reservations.reservationitem': {
            'Meta': {'object_name': 'ReservationItem'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'price': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        },
        'reservations.reservationnotificationemail': {
            'Meta': {'object_name': 'ReservationNotificationEmail'},
            'email': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['reservations']