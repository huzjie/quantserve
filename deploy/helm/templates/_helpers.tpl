{{- define "quantserve.name" -}}
{{- default .Chart.Name .Values.nameOverride | trunc 63 | trimSuffix "-" }}
{{- end }}

{{- define "quantserve.fullname" -}}
{{- if .Values.fullnameOverride }}{{ .Values.fullnameOverride }}
{{- else }}{{ .Release.Name }}-{{ include "quantserve.name" . }}{{- end }}
{{- end }}

{{- define "quantserve.labels" -}}
app.kubernetes.io/name: {{ include "quantserve.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
{{- end }}
