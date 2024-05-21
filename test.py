import norch
from norch.utils.data.dataloader import Dataloader
import norch
import norch.nn as nn
import norch.optim as optim
import random
random.seed(1)

"""one_hot_target = norch.one_hot_encode(norch.Tensor([5]), num_classes=10)
print(one_hot_target)"""

logits = norch.Tensor([[2.0, 1.0, 0.1, 0.1], [2.0, 1.0, 0.1, 0.1], [2.0, 1.0, 0.1, 0.1]], requires_grad=True)

# One-hot encoded target with shape (batch_size, num_classes)
one_hot_target = norch.Tensor([0, 1, 1])

criterion = nn.CrossEntropyLoss()

loss = criterion(logits, one_hot_target)
print(loss)


"""a = norch.Tensor([[[4.186502456665039]]])
b = norch.Tensor([[[2.0, 2.0,],[-1.0, -1.0,]],[[1.0, 2.0,],[3.0, 3.0,]]])

print(b)
print(a.shape)
print(b-a)"""

"""print(torch_tensor.shape)
print('\n\n')
torch_tensor2 = torch_tensor.max(axis=1)
print(torch_tensor2.shape)
print('\n\n')
c = torch_tensor + torch_tensor2
print(c)
"""

"""

to_tensor = lambda x: norch.Tensor(x)
reshape = lambda x: x.reshape([-1, 784])
transform = lambda x: reshape(to_tensor(x))
target_transform = lambda x: to_tensor(x)

train_data, test_data = norch.datasets.MNIST.splits(transform=transform, target_transform=target_transform)
sample, _ = train_data[0]

BATCH_SIZE = 100

train_loader = Dataloader(train_data, batch_size = BATCH_SIZE)

class MyModel(nn.Module):
    def __init__(self):
        super(MyModel, self).__init__()
        self.fc1 = nn.Linear(784, 10)
        self.sigmoid = nn.Sigmoid()
        self.fc2 = nn.Linear(10, 1)

    def forward(self, x):
        out = self.fc1(x)
        out = self.sigmoid(out)
        out = self.fc2(out)
        
        return out

device = "cpu"
epochs = 10

model = MyModel().to(device)
criterion = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=0.001)
loss_list = []

for epoch in range(epochs):    
    for idx, batch in enumerate(train_loader):
        x, target = batch

        x = x.T
        target = target.T 

        x = x.to(device)
        target = target.to(device)

        outputs = model(x)

        loss = criterion(outputs, target)
        
        optimizer.zero_grad()
        loss.backward()
        print('loss_antes', loss)

        print('f1 antes', model.fc1.bias)
        print('f1 grad_antes', model.fc1.bias.grad)
        print('f2 antes', model.fc2.bias)
        print('f2 grad_antes', model.fc2.bias.grad)

        optimizer.step()
        print('\n')

        print('f1 depois', model.fc1.bias)
        print('f2 depois', model.fc2.bias)
        print('\n\n')

    print(f'Epoch [{epoch + 1}/{epochs}], Loss: {loss[0]:.4f}')
    loss_list.append(loss[0])"""