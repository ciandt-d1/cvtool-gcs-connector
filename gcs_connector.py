import boto
import gcs_oauth2_boto_plugin

GOOGLE_STORAGE = 'gs'

LOCAL_FILE = 'file'

CLIENT_ID = 'fallback only'
CLIENT_SECRET = 'fallback only'
gcs_oauth2_boto_plugin.SetFallbackClientIdAndSecret(CLIENT_ID, CLIENT_SECRET)

uri = boto.storage_uri('gbim-dataflow-test', GOOGLE_STORAGE)
for obj in uri.get_bucket():
  print '%s://%s/%s' % (uri.scheme, uri.bucket_name, obj.name)
  #print '  "%s"' % obj.get_contents_as_string()