#ifndef CUDA_KERNEL_H_
#define CUDA_KERNEL_H_

    __host__ void cpu_to_cuda(Tensor* tensor);
    __host__ void cuda_to_cpu(Tensor* tensor);
    
    __global__ void add_tensor_cuda_kernel(float* data1, float* data2, float* result_data, int size);
    __host__ void add_tensor_cuda(Tensor* tensor1, Tensor* tensor2, float* result_data);
    
    __global__ void sum_tensor_cuda_kernel(float* data, float* result_data);
    __host__ void sum_tensor_cuda(Tensor* tensor, float* result_data);

    __global__ void sub_tensor_cuda_kernel(float* data1, float* data2, float* result_data, int size);
    __host__ void sub_tensor_cuda(Tensor* tensor1, Tensor* tensor2, float* result_data);
    
    __global__ void elementwise_mul_tensor_cuda_kernel(float* data1, float* data2, float* result_data, int size);
    __host__ void elementwise_mul_tensor_cuda(Tensor* tensor1, Tensor* tensor2, float* result_data);

    __global__ void scalar_mul_tensor_cuda_kernel(float* data, float scalar, float* result_data, int size);
    __host__ void scalar_mul_tensor_cuda(Tensor* tensor, float scalar, float* result_data);

    __global__ void matmul_tensor_cuda_kernel(float* data1, float* data2, float* result_data, int rows1, int cols1, int cols2);
    __host__ void matmul_tensor_cuda(Tensor* tensor1, Tensor* tensor2, float* result_data);

    __global__ void pow_tensor_cuda_kernel(float* data, float power, float* result_data, int size);
    __host__ void pow_tensor_cuda(Tensor* tensor, float power, float* result_data);

    __global__ void ones_like_tensor_cuda_kernel(float* data, float* result_data, int size);
    __host__ void ones_like_tensor_cuda(Tensor* tensor, float* result_data);

    __global__ void zeros_like_tensor_cuda_kernel(float* data, float* result_data, int size);
    __host__ void zeros_like_tensor_cuda(Tensor* tensor, float* result_data);

    __global__ void transpose_tensor_cuda_kernel(float* data, float* result_data, int rows, int cols);
    __host__ void transpose_tensor_cuda(Tensor* tensor, float* result_data);

    __global__ void assign_tensor_cuda_kernel(float* data, float* result_data, int size);
    __host__ void assign_tensor_cuda(Tensor* tensor, float* result_data);





#endif /* CUDA_KERNEL_H_ */
