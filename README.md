# rdkit-bq

[RDKit](https://www.rdkit.org/) provides a substantial amount of useful functionality related to computational chemistry and is used widely by scientists. [BigQuery](https://cloud.google.com/bigquery) (BQ) is a full-featured, fully managed, serverless Cloud data warehouse capable of scaling to very large data sets. While BQ provides an exceptionally broad range of functionality, it, understandably, does not provide domain-specific functionality, e.g. functionality related to computational chemistry. [BQ remote functions](https://cloud.google.com/bigquery/docs/reference/standard-sql/remote-functions) can be leveraged though to achieve a substantial level of integration between third party codes such as RDKit and BiqQuery.


Outlined below is an approach for integrating RDKit with BQ. Since RDKit relies on native code, the approach described here relies heavily on Cloud Run as the backing service. The sample code provided only aims to outline the overall approach and is not intended to serve as a production quality implementation. Performance and robustness are also not major considerations.


For the sake of simplicity, the code described here only makes available a fairly simplistic RDKit descriptor / property via BQ, i.e. molecular weight. The overall approach is extensible though and more sophisticated transformations can be implemented.
