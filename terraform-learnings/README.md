# installing terraform 
#
## 
add hashicorp gpg key
##
```
wget -O - https://apt.releases.hashicorp.com/gpg | sudo gpg --dearmor -o /usr/share/keyrings/hashicorp-archive-keyring.gpg
```

##
add hashicorp repository
##

```
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(grep -oP '(?<=UBUNTU_CODENAME=).*' /etc/os-release || lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/hashicorp.list

```

## 
install terraform
##

``` 
sudo apt install terraform
```

Run:
```
terraform init

```
It should now download the Kubernetes provider successfully.

Then you can proceed with:
```
terraform plan
terraform apply 
```
