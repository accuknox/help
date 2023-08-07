## Assets count

**compute.Subnetwork:** --asset-types=compute.googleapis.com/Subnetwork

```sh
gcloud asset search-all-resources --project=hopeful-vine-383309 --asset-types=compute.googleapis.com/Subnetwork --format='value(name)' | sort -u | find /c /v " "
```

**compute.Route:** --asset-types=compute.googleapis.com/Route

```sh
gcloud asset search-all-resources --project=hopeful-vine-383309 --asset-types=compute.googleapis.com/Route --format='value(name)' | sort -u | find /c /v " "
```

**compute.Firewall:** --asset-types=compute.googleapis.com/Firewall

```sh
gcloud asset search-all-resources --project=hopeful-vine-383309 --asset-types=compute.googleapis.com/Firewall --format='value(name)' | sort -u | find /c /v " "
```

**logging.LogBucket:** --asset-types=logging.googleapis.com/LogBucket

```sh
gcloud asset search-all-resources --project=hopeful-vine-383309 --asset-types=logging.googleapis.com/LogBucket --format='value(name)' | sort -u | find /c /v " "
```

**serviceusage.Service:** --asset-types=serviceusage.googleapis.com/Service

```sh
gcloud asset search-all-resources --project=hopeful-vine-383309 --asset-types=serviceusage.googleapis.com/Service --format='value(name)' | sort -u | find /c /v " "
```

## Bash script to get Assets Count

```sh
#!/bin/bash
Var1=$(gcloud asset search-all-resources --project=hopeful-vine-383309 --asset-types=compute.googleapis.com/Subnetwork --format='value(name)' | sort -u | wc -l)
Var2=$(gcloud asset search-all-resources --project=hopeful-vine-383309 --asset-types=compute.googleapis.com/Route --format='value(name)' | sort -u | wc -l)
Var3=$(gcloud asset search-all-resources --project=hopeful-vine-383309 --asset-types=compute.googleapis.com/Firewall --format='value(name)' | sort -u | wc -l)
Var4=$(gcloud asset search-all-resources --project=hopeful-vine-383309 --asset-types=logging.googleapis.com/LogBucket --format='value(name)' | sort -u | wc -l)
Var5=$(gcloud asset search-all-resources --project=hopeful-vine-383309 --asset-types=serviceusage.googleapis.com/Service --format='value(name)' | sort -u | wc -l)
(( SUM=Var1+Var2+Var3+Var4+Var5 ))
echo "Total number of Assets in your GCP account is $SUM"
```
## Sample Output

![](/getting-started/images/gcp-count.png)
