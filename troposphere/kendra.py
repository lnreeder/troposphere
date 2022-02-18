# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType, Tags
from .validators import boolean, double, integer


class DocumentAttributeValue(AWSProperty):
    """
    `DocumentAttributeValue <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-documentattributevalue.html>`__
    """

    props: PropsDictType = {
        "DateValue": (str, False),
        "LongValue": (integer, False),
        "StringListValue": ([str], False),
        "StringValue": (str, False),
    }


class DocumentAttributeCondition(AWSProperty):
    """
    `DocumentAttributeCondition <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-documentattributecondition.html>`__
    """

    props: PropsDictType = {
        "ConditionDocumentAttributeKey": (str, True),
        "ConditionOnValue": (DocumentAttributeValue, False),
        "Operator": (str, True),
    }


class HookConfiguration(AWSProperty):
    """
    `HookConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-hookconfiguration.html>`__
    """

    props: PropsDictType = {
        "InvocationCondition": (DocumentAttributeCondition, False),
        "LambdaArn": (str, True),
        "S3Bucket": (str, True),
    }


class DocumentAttributeTarget(AWSProperty):
    """
    `DocumentAttributeTarget <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-documentattributetarget.html>`__
    """

    props: PropsDictType = {
        "TargetDocumentAttributeKey": (str, True),
        "TargetDocumentAttributeValue": (DocumentAttributeValue, False),
        "TargetDocumentAttributeValueDeletion": (boolean, False),
    }


class InlineCustomDocumentEnrichmentConfiguration(AWSProperty):
    """
    `InlineCustomDocumentEnrichmentConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-inlinecustomdocumentenrichmentconfiguration.html>`__
    """

    props: PropsDictType = {
        "Condition": (DocumentAttributeCondition, False),
        "DocumentContentDeletion": (boolean, False),
        "Target": (DocumentAttributeTarget, False),
    }


class CustomDocumentEnrichmentConfiguration(AWSProperty):
    """
    `CustomDocumentEnrichmentConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-customdocumentenrichmentconfiguration.html>`__
    """

    props: PropsDictType = {
        "InlineConfigurations": ([InlineCustomDocumentEnrichmentConfiguration], False),
        "PostExtractionHookConfiguration": (HookConfiguration, False),
        "PreExtractionHookConfiguration": (HookConfiguration, False),
        "RoleArn": (str, False),
    }


class ConfluenceAttachmentToIndexFieldMapping(AWSProperty):
    """
    `ConfluenceAttachmentToIndexFieldMapping <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluenceattachmenttoindexfieldmapping.html>`__
    """

    props: PropsDictType = {
        "DataSourceFieldName": (str, True),
        "DateFieldFormat": (str, False),
        "IndexFieldName": (str, True),
    }


class ConfluenceAttachmentConfiguration(AWSProperty):
    """
    `ConfluenceAttachmentConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluenceattachmentconfiguration.html>`__
    """

    props: PropsDictType = {
        "AttachmentFieldMappings": ([ConfluenceAttachmentToIndexFieldMapping], False),
        "CrawlAttachments": (boolean, False),
    }


class ConfluenceBlogToIndexFieldMapping(AWSProperty):
    """
    `ConfluenceBlogToIndexFieldMapping <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluenceblogtoindexfieldmapping.html>`__
    """

    props: PropsDictType = {
        "DataSourceFieldName": (str, True),
        "DateFieldFormat": (str, False),
        "IndexFieldName": (str, True),
    }


class ConfluenceBlogConfiguration(AWSProperty):
    """
    `ConfluenceBlogConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluenceblogconfiguration.html>`__
    """

    props: PropsDictType = {
        "BlogFieldMappings": ([ConfluenceBlogToIndexFieldMapping], False),
    }


class ConfluencePageToIndexFieldMapping(AWSProperty):
    """
    `ConfluencePageToIndexFieldMapping <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluencepagetoindexfieldmapping.html>`__
    """

    props: PropsDictType = {
        "DataSourceFieldName": (str, True),
        "DateFieldFormat": (str, False),
        "IndexFieldName": (str, True),
    }


class ConfluencePageConfiguration(AWSProperty):
    """
    `ConfluencePageConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluencepageconfiguration.html>`__
    """

    props: PropsDictType = {
        "PageFieldMappings": ([ConfluencePageToIndexFieldMapping], False),
    }


class ConfluenceSpaceToIndexFieldMapping(AWSProperty):
    """
    `ConfluenceSpaceToIndexFieldMapping <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluencespacetoindexfieldmapping.html>`__
    """

    props: PropsDictType = {
        "DataSourceFieldName": (str, True),
        "DateFieldFormat": (str, False),
        "IndexFieldName": (str, True),
    }


class ConfluenceSpaceConfiguration(AWSProperty):
    """
    `ConfluenceSpaceConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluencespaceconfiguration.html>`__
    """

    props: PropsDictType = {
        "CrawlArchivedSpaces": (boolean, False),
        "CrawlPersonalSpaces": (boolean, False),
        "ExcludeSpaces": ([str], False),
        "IncludeSpaces": ([str], False),
        "SpaceFieldMappings": ([ConfluenceSpaceToIndexFieldMapping], False),
    }


class DataSourceVpcConfiguration(AWSProperty):
    """
    `DataSourceVpcConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-datasourcevpcconfiguration.html>`__
    """

    props: PropsDictType = {
        "SecurityGroupIds": ([str], True),
        "SubnetIds": ([str], True),
    }


class ConfluenceConfiguration(AWSProperty):
    """
    `ConfluenceConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluenceconfiguration.html>`__
    """

    props: PropsDictType = {
        "AttachmentConfiguration": (ConfluenceAttachmentConfiguration, False),
        "BlogConfiguration": (ConfluenceBlogConfiguration, False),
        "ExclusionPatterns": ([str], False),
        "InclusionPatterns": ([str], False),
        "PageConfiguration": (ConfluencePageConfiguration, False),
        "SecretArn": (str, True),
        "ServerUrl": (str, True),
        "SpaceConfiguration": (ConfluenceSpaceConfiguration, False),
        "Version": (str, True),
        "VpcConfiguration": (DataSourceVpcConfiguration, False),
    }


class AclConfiguration(AWSProperty):
    """
    `AclConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-aclconfiguration.html>`__
    """

    props: PropsDictType = {
        "AllowedGroupsColumnName": (str, True),
    }


class DataSourceToIndexFieldMapping(AWSProperty):
    """
    `DataSourceToIndexFieldMapping <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-datasourcetoindexfieldmapping.html>`__
    """

    props: PropsDictType = {
        "DataSourceFieldName": (str, True),
        "DateFieldFormat": (str, False),
        "IndexFieldName": (str, True),
    }


class ColumnConfiguration(AWSProperty):
    """
    `ColumnConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-columnconfiguration.html>`__
    """

    props: PropsDictType = {
        "ChangeDetectingColumns": ([str], True),
        "DocumentDataColumnName": (str, True),
        "DocumentIdColumnName": (str, True),
        "DocumentTitleColumnName": (str, False),
        "FieldMappings": ([DataSourceToIndexFieldMapping], False),
    }


class ConnectionConfiguration(AWSProperty):
    """
    `ConnectionConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-connectionconfiguration.html>`__
    """

    props: PropsDictType = {
        "DatabaseHost": (str, True),
        "DatabaseName": (str, True),
        "DatabasePort": (integer, True),
        "SecretArn": (str, True),
        "TableName": (str, True),
    }


class SqlConfiguration(AWSProperty):
    """
    `SqlConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-sqlconfiguration.html>`__
    """

    props: PropsDictType = {
        "QueryIdentifiersEnclosingOption": (str, False),
    }


class DatabaseConfiguration(AWSProperty):
    """
    `DatabaseConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-databaseconfiguration.html>`__
    """

    props: PropsDictType = {
        "AclConfiguration": (AclConfiguration, False),
        "ColumnConfiguration": (ColumnConfiguration, True),
        "ConnectionConfiguration": (ConnectionConfiguration, True),
        "DatabaseEngineType": (str, True),
        "SqlConfiguration": (SqlConfiguration, False),
        "VpcConfiguration": (DataSourceVpcConfiguration, False),
    }


class GoogleDriveConfiguration(AWSProperty):
    """
    `GoogleDriveConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-googledriveconfiguration.html>`__
    """

    props: PropsDictType = {
        "ExcludeMimeTypes": ([str], False),
        "ExcludeSharedDrives": ([str], False),
        "ExcludeUserAccounts": ([str], False),
        "ExclusionPatterns": ([str], False),
        "FieldMappings": ([DataSourceToIndexFieldMapping], False),
        "InclusionPatterns": ([str], False),
        "SecretArn": (str, True),
    }


class S3Path(AWSProperty):
    """
    `S3Path <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-faq-s3path.html>`__
    """

    props: PropsDictType = {
        "Bucket": (str, True),
        "Key": (str, True),
    }


class OneDriveUsers(AWSProperty):
    """
    `OneDriveUsers <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-onedriveusers.html>`__
    """

    props: PropsDictType = {
        "OneDriveUserList": ([str], False),
        "OneDriveUserS3Path": (S3Path, False),
    }


class OneDriveConfiguration(AWSProperty):
    """
    `OneDriveConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-onedriveconfiguration.html>`__
    """

    props: PropsDictType = {
        "DisableLocalGroups": (boolean, False),
        "ExclusionPatterns": ([str], False),
        "FieldMappings": ([DataSourceToIndexFieldMapping], False),
        "InclusionPatterns": ([str], False),
        "OneDriveUsers": (OneDriveUsers, True),
        "SecretArn": (str, True),
        "TenantDomain": (str, True),
    }


class AccessControlListConfiguration(AWSProperty):
    """
    `AccessControlListConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-accesscontrollistconfiguration.html>`__
    """

    props: PropsDictType = {
        "KeyPath": (str, False),
    }


class DocumentsMetadataConfiguration(AWSProperty):
    """
    `DocumentsMetadataConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-documentsmetadataconfiguration.html>`__
    """

    props: PropsDictType = {
        "S3Prefix": (str, False),
    }


class S3DataSourceConfiguration(AWSProperty):
    """
    `S3DataSourceConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-s3datasourceconfiguration.html>`__
    """

    props: PropsDictType = {
        "AccessControlListConfiguration": (AccessControlListConfiguration, False),
        "BucketName": (str, True),
        "DocumentsMetadataConfiguration": (DocumentsMetadataConfiguration, False),
        "ExclusionPatterns": ([str], False),
        "InclusionPatterns": ([str], False),
        "InclusionPrefixes": ([str], False),
    }


class SalesforceChatterFeedConfiguration(AWSProperty):
    """
    `SalesforceChatterFeedConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforcechatterfeedconfiguration.html>`__
    """

    props: PropsDictType = {
        "DocumentDataFieldName": (str, True),
        "DocumentTitleFieldName": (str, False),
        "FieldMappings": ([DataSourceToIndexFieldMapping], False),
        "IncludeFilterTypes": ([str], False),
    }


class SalesforceCustomKnowledgeArticleTypeConfiguration(AWSProperty):
    """
    `SalesforceCustomKnowledgeArticleTypeConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforcecustomknowledgearticletypeconfiguration.html>`__
    """

    props: PropsDictType = {
        "DocumentDataFieldName": (str, True),
        "DocumentTitleFieldName": (str, False),
        "FieldMappings": ([DataSourceToIndexFieldMapping], False),
        "Name": (str, True),
    }


class SalesforceStandardKnowledgeArticleTypeConfiguration(AWSProperty):
    """
    `SalesforceStandardKnowledgeArticleTypeConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforcestandardknowledgearticletypeconfiguration.html>`__
    """

    props: PropsDictType = {
        "DocumentDataFieldName": (str, True),
        "DocumentTitleFieldName": (str, False),
        "FieldMappings": ([DataSourceToIndexFieldMapping], False),
    }


class SalesforceKnowledgeArticleConfiguration(AWSProperty):
    """
    `SalesforceKnowledgeArticleConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforceknowledgearticleconfiguration.html>`__
    """

    props: PropsDictType = {
        "CustomKnowledgeArticleTypeConfigurations": (
            [SalesforceCustomKnowledgeArticleTypeConfiguration],
            False,
        ),
        "IncludedStates": ([str], True),
        "StandardKnowledgeArticleTypeConfiguration": (
            SalesforceStandardKnowledgeArticleTypeConfiguration,
            False,
        ),
    }


class SalesforceStandardObjectAttachmentConfiguration(AWSProperty):
    """
    `SalesforceStandardObjectAttachmentConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforcestandardobjectattachmentconfiguration.html>`__
    """

    props: PropsDictType = {
        "DocumentTitleFieldName": (str, False),
        "FieldMappings": ([DataSourceToIndexFieldMapping], False),
    }


class SalesforceStandardObjectConfiguration(AWSProperty):
    """
    `SalesforceStandardObjectConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforcestandardobjectconfiguration.html>`__
    """

    props: PropsDictType = {
        "DocumentDataFieldName": (str, True),
        "DocumentTitleFieldName": (str, False),
        "FieldMappings": ([DataSourceToIndexFieldMapping], False),
        "Name": (str, True),
    }


class SalesforceConfiguration(AWSProperty):
    """
    `SalesforceConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforceconfiguration.html>`__
    """

    props: PropsDictType = {
        "ChatterFeedConfiguration": (SalesforceChatterFeedConfiguration, False),
        "CrawlAttachments": (boolean, False),
        "ExcludeAttachmentFilePatterns": ([str], False),
        "IncludeAttachmentFilePatterns": ([str], False),
        "KnowledgeArticleConfiguration": (
            SalesforceKnowledgeArticleConfiguration,
            False,
        ),
        "SecretArn": (str, True),
        "ServerUrl": (str, True),
        "StandardObjectAttachmentConfiguration": (
            SalesforceStandardObjectAttachmentConfiguration,
            False,
        ),
        "StandardObjectConfigurations": (
            [SalesforceStandardObjectConfiguration],
            False,
        ),
    }


class ServiceNowKnowledgeArticleConfiguration(AWSProperty):
    """
    `ServiceNowKnowledgeArticleConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-servicenowknowledgearticleconfiguration.html>`__
    """

    props: PropsDictType = {
        "CrawlAttachments": (boolean, False),
        "DocumentDataFieldName": (str, True),
        "DocumentTitleFieldName": (str, False),
        "ExcludeAttachmentFilePatterns": ([str], False),
        "FieldMappings": ([DataSourceToIndexFieldMapping], False),
        "FilterQuery": (str, False),
        "IncludeAttachmentFilePatterns": ([str], False),
    }


class ServiceNowServiceCatalogConfiguration(AWSProperty):
    """
    `ServiceNowServiceCatalogConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-servicenowservicecatalogconfiguration.html>`__
    """

    props: PropsDictType = {
        "CrawlAttachments": (boolean, False),
        "DocumentDataFieldName": (str, True),
        "DocumentTitleFieldName": (str, False),
        "ExcludeAttachmentFilePatterns": ([str], False),
        "FieldMappings": ([DataSourceToIndexFieldMapping], False),
        "IncludeAttachmentFilePatterns": ([str], False),
    }


class ServiceNowConfiguration(AWSProperty):
    """
    `ServiceNowConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-servicenowconfiguration.html>`__
    """

    props: PropsDictType = {
        "AuthenticationType": (str, False),
        "HostUrl": (str, True),
        "KnowledgeArticleConfiguration": (
            ServiceNowKnowledgeArticleConfiguration,
            False,
        ),
        "SecretArn": (str, True),
        "ServiceCatalogConfiguration": (ServiceNowServiceCatalogConfiguration, False),
        "ServiceNowBuildVersion": (str, True),
    }


class SharePointConfiguration(AWSProperty):
    """
    `SharePointConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-sharepointconfiguration.html>`__
    """

    props: PropsDictType = {
        "CrawlAttachments": (boolean, False),
        "DisableLocalGroups": (boolean, False),
        "DocumentTitleFieldName": (str, False),
        "ExclusionPatterns": ([str], False),
        "FieldMappings": ([DataSourceToIndexFieldMapping], False),
        "InclusionPatterns": ([str], False),
        "SecretArn": (str, True),
        "SharePointVersion": (str, True),
        "SslCertificateS3Path": (S3Path, False),
        "Urls": ([str], True),
        "UseChangeLog": (boolean, False),
        "VpcConfiguration": (DataSourceVpcConfiguration, False),
    }


class ProxyConfiguration(AWSProperty):
    """
    `ProxyConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-proxyconfiguration.html>`__
    """

    props: PropsDictType = {
        "Credentials": (str, False),
        "Host": (str, True),
        "Port": (integer, True),
    }


class WebCrawlerBasicAuthentication(AWSProperty):
    """
    `WebCrawlerBasicAuthentication <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-webcrawlerbasicauthentication.html>`__
    """

    props: PropsDictType = {
        "Credentials": (str, True),
        "Host": (str, True),
        "Port": (integer, True),
    }


class WebCrawlerAuthenticationConfiguration(AWSProperty):
    """
    `WebCrawlerAuthenticationConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-webcrawlerauthenticationconfiguration.html>`__
    """

    props: PropsDictType = {
        "BasicAuthentication": ([WebCrawlerBasicAuthentication], False),
    }


class WebCrawlerSeedUrlConfiguration(AWSProperty):
    """
    `WebCrawlerSeedUrlConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-webcrawlerseedurlconfiguration.html>`__
    """

    props: PropsDictType = {
        "SeedUrls": ([str], True),
        "WebCrawlerMode": (str, False),
    }


class WebCrawlerSiteMapsConfiguration(AWSProperty):
    """
    `WebCrawlerSiteMapsConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-webcrawlersitemapsconfiguration.html>`__
    """

    props: PropsDictType = {
        "SiteMaps": ([str], True),
    }


class WebCrawlerUrls(AWSProperty):
    """
    `WebCrawlerUrls <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-webcrawlerurls.html>`__
    """

    props: PropsDictType = {
        "SeedUrlConfiguration": (WebCrawlerSeedUrlConfiguration, False),
        "SiteMapsConfiguration": (WebCrawlerSiteMapsConfiguration, False),
    }


class WebCrawlerConfiguration(AWSProperty):
    """
    `WebCrawlerConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-webcrawlerconfiguration.html>`__
    """

    props: PropsDictType = {
        "AuthenticationConfiguration": (WebCrawlerAuthenticationConfiguration, False),
        "CrawlDepth": (integer, False),
        "MaxContentSizePerPageInMegaBytes": (double, False),
        "MaxLinksPerPage": (integer, False),
        "MaxUrlsPerMinuteCrawlRate": (integer, False),
        "ProxyConfiguration": (ProxyConfiguration, False),
        "UrlExclusionPatterns": ([str], False),
        "UrlInclusionPatterns": ([str], False),
        "Urls": (WebCrawlerUrls, True),
    }


class WorkDocsConfiguration(AWSProperty):
    """
    `WorkDocsConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-workdocsconfiguration.html>`__
    """

    props: PropsDictType = {
        "CrawlComments": (boolean, False),
        "ExclusionPatterns": ([str], False),
        "FieldMappings": ([DataSourceToIndexFieldMapping], False),
        "InclusionPatterns": ([str], False),
        "OrganizationId": (str, True),
        "UseChangeLog": (boolean, False),
    }


class DataSourceConfiguration(AWSProperty):
    """
    `DataSourceConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-datasourceconfiguration.html>`__
    """

    props: PropsDictType = {
        "ConfluenceConfiguration": (ConfluenceConfiguration, False),
        "DatabaseConfiguration": (DatabaseConfiguration, False),
        "GoogleDriveConfiguration": (GoogleDriveConfiguration, False),
        "OneDriveConfiguration": (OneDriveConfiguration, False),
        "S3Configuration": (S3DataSourceConfiguration, False),
        "SalesforceConfiguration": (SalesforceConfiguration, False),
        "ServiceNowConfiguration": (ServiceNowConfiguration, False),
        "SharePointConfiguration": (SharePointConfiguration, False),
        "WebCrawlerConfiguration": (WebCrawlerConfiguration, False),
        "WorkDocsConfiguration": (WorkDocsConfiguration, False),
    }


class DataSource(AWSObject):
    """
    `DataSource <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-datasource.html>`__
    """

    resource_type = "AWS::Kendra::DataSource"

    props: PropsDictType = {
        "CustomDocumentEnrichmentConfiguration": (
            CustomDocumentEnrichmentConfiguration,
            False,
        ),
        "DataSourceConfiguration": (DataSourceConfiguration, False),
        "Description": (str, False),
        "IndexId": (str, True),
        "Name": (str, True),
        "RoleArn": (str, False),
        "Schedule": (str, False),
        "Tags": (Tags, False),
        "Type": (str, True),
    }


class Faq(AWSObject):
    """
    `Faq <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-faq.html>`__
    """

    resource_type = "AWS::Kendra::Faq"

    props: PropsDictType = {
        "Description": (str, False),
        "FileFormat": (str, False),
        "IndexId": (str, True),
        "Name": (str, True),
        "RoleArn": (str, True),
        "S3Path": (S3Path, True),
        "Tags": (Tags, False),
    }


class CapacityUnitsConfiguration(AWSProperty):
    """
    `CapacityUnitsConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-capacityunitsconfiguration.html>`__
    """

    props: PropsDictType = {
        "QueryCapacityUnits": (integer, True),
        "StorageCapacityUnits": (integer, True),
    }


class ValueImportanceItem(AWSProperty):
    """
    `ValueImportanceItem <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-valueimportanceitem.html>`__
    """

    props: PropsDictType = {
        "Key": (str, False),
        "Value": (integer, False),
    }


class Relevance(AWSProperty):
    """
    `Relevance <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-relevance.html>`__
    """

    props: PropsDictType = {
        "Duration": (str, False),
        "Freshness": (boolean, False),
        "Importance": (integer, False),
        "RankOrder": (str, False),
        "ValueImportanceItems": ([ValueImportanceItem], False),
    }


class Search(AWSProperty):
    """
    `Search <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-search.html>`__
    """

    props: PropsDictType = {
        "Displayable": (boolean, False),
        "Facetable": (boolean, False),
        "Searchable": (boolean, False),
        "Sortable": (boolean, False),
    }


class DocumentMetadataConfiguration(AWSProperty):
    """
    `DocumentMetadataConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-documentmetadataconfiguration.html>`__
    """

    props: PropsDictType = {
        "Name": (str, True),
        "Relevance": (Relevance, False),
        "Search": (Search, False),
        "Type": (str, True),
    }


class ServerSideEncryptionConfiguration(AWSProperty):
    """
    `ServerSideEncryptionConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-serversideencryptionconfiguration.html>`__
    """

    props: PropsDictType = {
        "KmsKeyId": (str, False),
    }


class JsonTokenTypeConfiguration(AWSProperty):
    """
    `JsonTokenTypeConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-jsontokentypeconfiguration.html>`__
    """

    props: PropsDictType = {
        "GroupAttributeField": (str, True),
        "UserNameAttributeField": (str, True),
    }


class JwtTokenTypeConfiguration(AWSProperty):
    """
    `JwtTokenTypeConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-jwttokentypeconfiguration.html>`__
    """

    props: PropsDictType = {
        "ClaimRegex": (str, False),
        "GroupAttributeField": (str, False),
        "Issuer": (str, False),
        "KeyLocation": (str, True),
        "SecretManagerArn": (str, False),
        "URL": (str, False),
        "UserNameAttributeField": (str, False),
    }


class UserTokenConfiguration(AWSProperty):
    """
    `UserTokenConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-usertokenconfiguration.html>`__
    """

    props: PropsDictType = {
        "JsonTokenTypeConfiguration": (JsonTokenTypeConfiguration, False),
        "JwtTokenTypeConfiguration": (JwtTokenTypeConfiguration, False),
    }


class Index(AWSObject):
    """
    `Index <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-index.html>`__
    """

    resource_type = "AWS::Kendra::Index"

    props: PropsDictType = {
        "CapacityUnits": (CapacityUnitsConfiguration, False),
        "Description": (str, False),
        "DocumentMetadataConfigurations": ([DocumentMetadataConfiguration], False),
        "Edition": (str, True),
        "Name": (str, True),
        "RoleArn": (str, True),
        "ServerSideEncryptionConfiguration": (ServerSideEncryptionConfiguration, False),
        "Tags": (Tags, False),
        "UserContextPolicy": (str, False),
        "UserTokenConfigurations": ([UserTokenConfiguration], False),
    }
