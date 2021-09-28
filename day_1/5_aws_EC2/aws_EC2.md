---
marp: true
theme: default
paginate: true
---

<style>
img[alt~="center"] {
  display: block;
  margin: 0 auto;
}
</style>

# Amazon Elastic Compute Cloud: EC2

---

- Uno de los servicios más antiguos en AWS.
- Nos permite deplegar máquinas virtuales en AWS.

---



reconfigured templates for your instances, known as Amazon Machine Images (AMIs), that package the bits you need for your server (including the operating system and additional software)

Various configurations of CPU, memory, storage, and networking capacity for your instances, known as instance types

Secure login information for your instances using key pairs (AWS stores the public key, and you store the private key in a secure place)

Storage volumes for temporary data that's deleted when you stop, hibernate, or terminate your instance, known as instance store volumes

Persistent storage volumes for your data using Amazon Elastic Block Store (Amazon EBS), known as Amazon EBS volumes

Multiple physical locations for your resources, such as instances and Amazon EBS volumes, known as Regions and Availability Zones

A firewall that enables you to specify the protocols, ports, and source IP ranges that can reach your instances using security groups

Static IPv4 addresses for dynamic cloud computing, known as Elastic IP addresses

Metadata, known as tags, that you can create and assign to your Amazon EC2 resources

Virtual networks you can create that are logically isolated from the rest of the AWS Cloud, and that you can optionally connect to your own network, known as virtual private clouds (VPCs)



An instance is a virtual server in the cloud. Its configuration at launch is a copy of the AMI that you specified when you launched the instance.

You can launch different types of instances from a single AMI. An instance type essentially determines the hardware of the host computer used for your instance. 

After you launch an instance, it looks like a traditional host, and you can interact with it as you would any computer. You have complete control of your instances; you can use sudo to run commands that require root privileges. 






The instance is an Amazon EBS-backed instance (meaning that the root volume is an EBS volume). You can either specify the Availability Zone in which your instance runs, or let Amazon EC2 select an Availability Zone for you. When you launch your instance, you secure it by specifying a key pair and security group. When you connect to your instance, you must specify the private key of the key pair that you specified when launching your instance. 






An Amazon Machine Image (AMI) provides the information required to launch an instance. You must specify an AMI when you launch an instance. You can launch multiple instances from a single AMI when you need multiple instances with the same configuration. You can use different AMIs to launch instances when you need instances with different configurations.

An AMI includes the following:

    One or more Amazon Elastic Block Store (Amazon EBS) snapshots, or, for instance-store-backed AMIs, a template for the root volume of the instance (for example, an operating system, an application server, and applications).

    Launch permissions that control which AWS accounts can use the AMI to launch instances.

    A block device mapping that specifies the volumes to attach to the instance when it's launched.










scp -i test.pem extracted_2018_RV_TICK_A_MFII_RV_TICK_A_20180319.TXT ec2-user@ec2-52-47-111-77.eu-west-3.compute.amazonaws.com:/home/ec2-user


## EC2 para Deep Learning.


