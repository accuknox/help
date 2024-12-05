# ModelArmor Use Cases

**ModelArmor** uses KubeArmor as a sandboxing engine to ensure that the untrusted models execution is constrained and within required checks. AI/ML Models are essentially processes and allowing untrusted models to execute in AI environments have significant risks such as possibility of cryptomining attacks leveraging GPUs, remote command injections, etc. KubeArmor's preemptive mitigation mechanism provides a suitable framework for constraining the execution environment of models.

The below examples show some of the important use-cases.

## **PyTorch Based Use Cases**

::cards:: cols=3

- title: Pickle Code Injection PoC
  content:
  image: ./icons/sql-injection.svg
  url: /use-cases/modelarmor-deploy-pytorch/

- title: Adversarial Attacks on Deep Learning Models
  content:
  image: ./icons/container-image-scan.svg
  url: /use-cases/modelarmor-adverserial-attacks/

- title: PyTorch App Deployment with KubeArmor
  content:
  image: ./icons/cluster-misconfig-scan.svg
  url: /use-cases/modelarmor-pickle-code/

::/cards::


## **TensorFlow Based Use Cases**

### FGSM Attack on a TensorFlow Model

<iframe src="https://drive.google.com/file/d/1EnmsIiR4G4bYmoxBIHTk1bDkW2XatM4N/preview" width="1000" height="480" allow="autoplay"></iframe>

### Keras Inject Attack and Apply Policies

<iframe src="https://drive.google.com/file/d/1olGBz3WUoJqmcAVdRY7uImKTHggRX6nK/preview" width="1000" height="480" allow="autoplay"></iframe>

## **Securing NVIDIA NIM**

<div>
  <iframe id="inlineFrameManual"
      title="Inline Frame Manual"
      width="150%"
      height="850"
      src="/resources/Securing_NVIDIA_NIM.pdf">
  </iframe>
</div>
