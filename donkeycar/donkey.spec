kind: PersistentVolumeClaim
apiVersion: v1
metadata:
  name: data
spec:
  accessModes:
    - ReadWriteOnce
  volumeMode: Filesystem
  resources:
    requests:
      storage: 100Gi
---
apiVersion: v1
kind: ReplicationController
metadata:
  name: donkeycar
spec:
  replicas: 1
  selector:
    role: donkeycar
  template:
    metadata:
      labels:
        role: donkeycar
    spec:
      containers:
      - name: donkeycar
        image: sapcc/donkeycar:v201905231120
        command: ["/bin/sh", "-ec", "tail -f /dev/null"]
        volumeMounts:
          - mountPath: /data
            name: data
      - name: pause
        image: gcr.io/google_containers/pause-amd64:3.0 
      volumes:
        - name: data
          persistentVolumeClaim:
            claimName: data
