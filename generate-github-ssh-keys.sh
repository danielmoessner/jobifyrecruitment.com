echo "GENERATING PRIVATE PUBLIC KEY PAIR"
ssh-keygen -t rsa
echo "COPY THIS INTO THE GITHUB WORKFLOW"
cat ~/.ssh/id_rsa
echo "ADD THE PUBLIC KEY TO THE AUTHORIZED KEYS"
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
echo "DEPLOY NOW AND TEST IF IT WORKS"
