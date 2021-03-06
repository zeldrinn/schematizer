# -*- coding: utf-8 -*-
# Copyright 2016 Yelp Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
"""This module contains the responses of schematizer v1 APIs.

Most of them are shared in various API responses, and therefore keep them
in this module.
"""
from __future__ import absolute_import
from __future__ import unicode_literals

from data_pipeline_avro_util.data_pipeline.avro_meta_data \
    import AvroMetaDataKeys

from schematizer.helpers.formatting import _format_datetime


def get_namespace_response_from_namespace(namespace):
    return {
        'namespace_id': namespace.id,
        'name': namespace.name,
        'created_at': _format_datetime(namespace.created_at),
        'updated_at': _format_datetime(namespace.updated_at)
    }


def get_source_response_from_source(source):
    return {
        'source_id': source.id,
        'name': source.name,
        'owner_email': source.owner_email,
        'namespace': get_namespace_response_from_namespace(source.namespace),
        'category': (
            None if source.category is None else source.category.category
        ),
        'created_at': _format_datetime(source.created_at),
        'updated_at': _format_datetime(source.updated_at)
    }


def get_topic_response_from_topic(topic):
    return {
        'topic_id': topic.id,
        'name': topic.name,
        'source': get_source_response_from_source(topic.source),
        'contains_pii': topic.contains_pii,
        'cluster_type': topic.cluster_type,
        'primary_keys': topic.primary_keys,
        'created_at': _format_datetime(topic.created_at),
        'updated_at': _format_datetime(topic.updated_at)
    }


def get_schema_response_from_avro_schema(avro_schema):
    response = {
        'schema_id': avro_schema.id,
        'schema': avro_schema.avro_schema,
        'status': avro_schema.status,
        'topic': get_topic_response_from_topic(avro_schema.topic),
        'primary_keys': avro_schema.avro_schema_json.get(
            AvroMetaDataKeys.PRIMARY_KEY,
            []
        ),
        'note': get_note_response_from_note(avro_schema.note),
        'created_at': _format_datetime(avro_schema.created_at),
        'updated_at': _format_datetime(avro_schema.updated_at)
    }
    # Since swagger cannot take null or None value for integer type,
    # here we just simply strip out this field.
    if avro_schema.base_schema_id is not None:
        response['base_schema_id'] = avro_schema.base_schema_id
    return response


def get_note_response_from_note(note):
    if note is not None:
        response = {
            'id': note.id,
            'reference_type': note.reference_type,
            'reference_id': note.reference_id,
            'note': note.note,
            'last_updated_by': note.last_updated_by,
            'created_at': _format_datetime(note.created_at),
            'updated_at': _format_datetime(note.updated_at)
        }
        return response
    return None


def get_category_response_from_source_category(source_category):
    return {
        'source_id': source_category.source_id,
        'category': source_category.category,
        'created_at': _format_datetime(source_category.created_at),
        'updated_at': _format_datetime(source_category.updated_at)
    }


def get_refresh_response_from_refresh(refresh):
    return {
        'refresh_id': refresh.id,
        'source_name': refresh.source.name,
        'namespace_name': refresh.source.namespace.name,
        'status': refresh.status,
        'offset': refresh.offset,
        'batch_size': refresh.batch_size,
        'priority': refresh.priority,
        'filter_condition': refresh.filter_condition,
        'avg_rows_per_second_cap': refresh.avg_rows_per_second_cap,
        'created_at': _format_datetime(refresh.created_at),
        'updated_at': _format_datetime(refresh.updated_at)
    }


def get_data_target_response_from_data_target(data_target):
    return {
        'data_target_id': data_target.id,
        'name': data_target.name,
        'target_type': data_target.target_type,
        'destination': data_target.destination,
        'created_at': _format_datetime(data_target.created_at),
        'updated_at': _format_datetime(data_target.updated_at)
    }


def get_consumer_group_response_from_consumer_group(consumer_group):
    return {
        'consumer_group_id': consumer_group.id,
        'group_name': consumer_group.group_name,
        'data_target': get_data_target_response_from_data_target(
            consumer_group.data_target
        ),
        'created_at': _format_datetime(consumer_group.created_at),
        'updated_at': _format_datetime(consumer_group.updated_at)
    }


def get_response_from_consumer_group_data_source(consumer_group_data_source):
    return {
        'consumer_group_data_source_id': consumer_group_data_source.id,
        'data_source_type': consumer_group_data_source.data_source_type,
        'data_source_id': consumer_group_data_source.data_source_id,
        'consumer_group_id': consumer_group_data_source.consumer_group_id,
        'created_at': _format_datetime(
            consumer_group_data_source.created_at
        ),
        'updated_at': _format_datetime(
            consumer_group_data_source.updated_at
        )
    }


def get_element_response_from_element(element):
    return {
        'id': element.id,
        'schema_id': element.avro_schema_id,
        'element_type': element.element_type,
        'key': element.key,
        'doc': element.doc,
        'note': get_note_response_from_note(element.note),
        'created_at': _format_datetime(element.created_at),
        'updated_at': _format_datetime(element.updated_at),
    }


def get_meta_attr_mapping_response(entity_type, entity_id, meta_attr_id):
    return {
        entity_type: int(entity_id),
        'meta_attribute_schema_id': meta_attr_id
    }
