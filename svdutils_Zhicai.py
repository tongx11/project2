# Solution set for CS 155 Set 6, 2016/2017
# Authors: Fabian Boemer, Sid Murching, Suraj Nair

import numpy as np

def grad_U(Ui, Yij, Vj, reg, eta, ai = 0.0, bj=0.0):
    """
    Takes as input Ui (the ith row of U), a training point Yij, the column
    vector Vj (jth column of V^T), reg (the regularization parameter lambda),
    and eta (the learning rate).

    Returns the gradient of the regularized loss function with
    respect to Ui multiplied by eta.
    """
    return reg*Ui - Vj * (Yij - np.dot(Ui, Vj) - ai - bj)
     
    

def grad_V(Vj, Yij, Ui, reg, eta, ai = 0.0, bj=0.0):
    """
    Takes as input the column vector Vj (jth column of V^T), a training point Yij,
    Ui (the ith row of U), reg (the regularization parameter lambda),
    and eta (the learning rate).

    Returns the gradient of the regularized loss function with
    respect to Vj multiplied by eta.
    """
    return reg*Vj - Ui * (Yij - np.dot(Ui, Vj) - ai - bj)

def grad_a(Ui, Yij, Vj, reg, eta, ai = 0.0, bj=0.0):
    return reg*ai - (Yij - np.dot(Ui, Vj) - ai - bj)

def grad_b(Ui, Yij, Vj, reg, eta, ai = 0.0, bj=0.0):
    return reg*bj - (Yij - np.dot(Ui, Vj) - ai - bj)

def get_err(U, V, Y, reg=0.0):
    """
    Takes as input a matrix Y of triples (i, j, Y_ij) where i is the index of a user,
    j is the index of a movie, and Y_ij is user i's rating of movie j and
    user/movie matrices U and V.
    
    Returns the mean regularized squared-error of predictions made by
    estimating Y_{ij} as the dot product of the ith row of U and the jth column of V^T.
    """
    #U: MxK
    #V: NxK
    #Y: MxN
    sum_Y_diff = 0.0
    for idx in range(len(Y)):
        idx_ui = Y[idx][0]-1
        idx_vj = Y[idx][1]-1
        Yij = Y[idx][2]
        Ui = U[idx_ui,:] #i-th row of U
        Vj = V[idx_vj,:] #j-th column of V^T, which is the j-th row of V
        sum_Y_diff += (Yij - np.dot(Ui, Vj))**2
    #U_fro = np.linalg.norm(U, ord='fro')
    #V_fro = np.linalg.norm(V, ord='fro')
    #return (reg*(U_fro**2 + V_fro**2) + sum_Y_diff)/(len(Y)*2.0)
    return sum_Y_diff/(len(Y)*2.0)      

def get_err_bias(U, V, Y, a, b, reg=0.0):
    """
    Takes as input a matrix Y of triples (i, j, Y_ij) where i is the index of a user,
    j is the index of a movie, and Y_ij is user i's rating of movie j and
    user/movie matrices U and V.
    
    Returns the mean regularized squared-error of predictions made by
    estimating Y_{ij} as the dot product of the ith row of U and the jth column of V^T.
    """
    #U: MxK
    #V: NxK
    #Y: MxN
    #a: M
    #b: N
    sum_Y_diff = 0.0
    for idx in range(len(Y)):
        idx_ui = Y[idx][0]-1
        idx_vj = Y[idx][1]-1
        Yij = Y[idx][2]
        Ui = U[idx_ui,:] #i-th row of U
        Vj = V[idx_vj,:] #j-th column of V^T, which is the j-th row of V
        sum_Y_diff += (Yij - np.dot(Ui, Vj) - a[idx_ui] - b[idx_vj])**2
    #U_fro = np.linalg.norm(U, ord='fro')
    #V_fro = np.linalg.norm(V, ord='fro')
    #return (reg*(U_fro**2 + V_fro**2) + sum_Y_diff)/(len(Y)*2.0)
    return sum_Y_diff/(len(Y)*2.0)      

def train_model(M, N, K, eta, reg, Y, eps=0.0001, max_epochs=300, debug=False):
    """
    Given a training data matrix Y containing rows (i, j, Y_ij)
    where Y_ij is user i's rating on movie j, learns an
    M x K matrix U and N x K matrix V such that rating Y_ij is approximated
    by (UV^T)_ij.

    Uses a learning rate of <eta> and regularization of <reg>. Stops after
    <max_epochs> epochs, or once the magnitude of the decrease in regularized
    MSE between epochs is smaller than a fraction <eps> of the decrease in
    MSE after the first epoch.

    Returns a tuple (U, V, err) consisting of U, V, and the unregularized MSE
    of the model.
    """
    
    U_train = np.random.rand(M,K) - 0.5
    V_train = np.random.rand(N,K) - 0.5
    errores = np.zeros(max_epochs)
    error_zero = get_err(U_train, V_train, Y, reg)
    error_one = 0.0
    if debug:
        print("Initial error = "+str(error_zero))
    for i_epoch in range(max_epochs):
        if i_epoch == 1:
            error_one = get_err(U_train, V_train, Y, reg)
        
        error_tm1 = get_err(U_train, V_train, Y, reg)
        #first, create an index array which is used as the order of the points we go through\
        ind_array = np.arange(len(Y)) #0 to N-1
        np.random.shuffle(ind_array)

        #loop over each point in the dataset
        for idx in ind_array:
            idx_ui = Y[idx][0]-1
            idx_vj = Y[idx][1]-1
            Yij = Y[idx][2]
            #update one row of U:
            gradient_this_U = grad_U(U_train[idx_ui,:], Yij, V_train[idx_vj,:], reg, eta)
            U_train[idx_ui,:] = np.copy(U_train[idx_ui,:] - eta*gradient_this_U)
            #update one column of V:
            gradient_this_V = grad_V(V_train[idx_vj,:], Yij, U_train[idx_ui,:], reg, eta)
            V_train[idx_vj,:] = np.copy(V_train[idx_vj,:] - eta*gradient_this_V)
        error_t = get_err(U_train, V_train, Y, reg)
        errores[i_epoch] = error_t
        eps_this = abs(error_t - error_tm1)/abs(error_one - error_zero)
        if debug:
            print("After epoch: "+str(i_epoch)+", error = "+str(error_t)+", eps = "+str(eps_this))
        if i_epoch > 1 and eps_this < eps:
            break
            
    error = get_err(U_train, V_train, Y, reg)
        
    return U_train, V_train, error

def train_model_bias(M, N, K, eta, reg, Y, eps=0.0001, max_epochs=300, debug=False):
    """
    Given a training data matrix Y containing rows (i, j, Y_ij)
    where Y_ij is user i's rating on movie j, learns an
    M x K matrix U and N x K matrix V such that rating Y_ij is approximated
    by (UV^T)_ij.

    Uses a learning rate of <eta> and regularization of <reg>. Stops after
    <max_epochs> epochs, or once the magnitude of the decrease in regularized
    MSE between epochs is smaller than a fraction <eps> of the decrease in
    MSE after the first epoch.

    Returns a tuple (U, V, err) consisting of U, V, and the unregularized MSE
    of the model.
    """
    
    U_train = np.random.rand(M,K) - 0.5
    V_train = np.random.rand(N,K) - 0.5
    a_train = np.random.rand(M) - 0.5
    b_train = np.random.rand(N) - 0.5
    
    errores = np.zeros(max_epochs)
    error_zero = get_err_bias(U_train, V_train, Y, a_train, b_train, reg)
    error_one = 0.0
    if debug:
        print("Initial error = "+str(error_zero))
    for i_epoch in range(max_epochs):
        if i_epoch == 1:
            error_one = get_err_bias(U_train, V_train, Y, a_train, b_train, reg)
        
        error_tm1 = get_err_bias(U_train, V_train, Y, a_train, b_train, reg)
        #first, create an index array which is used as the order of the points we go through\
        ind_array = np.arange(len(Y)) #0 to N-1
        np.random.shuffle(ind_array)

        #loop over each point in the dataset
        for idx in ind_array:
            idx_ui = Y[idx][0]-1
            idx_vj = Y[idx][1]-1
            Yij = Y[idx][2]
            #update one row of U:
            gradient_this_U = grad_U(U_train[idx_ui,:], Yij, V_train[idx_vj,:], reg, eta)
            U_train[idx_ui,:] = np.copy(U_train[idx_ui,:] - eta*gradient_this_U)
            #update one column of V:
            gradient_this_V = grad_V(V_train[idx_vj,:], Yij, U_train[idx_ui,:], reg, eta)
            V_train[idx_vj,:] = np.copy(V_train[idx_vj,:] - eta*gradient_this_V)
            #update ai
            gradient_this_a = grad_a(U_train[idx_ui,:], Yij, V_train[idx_vj,:], reg, eta, a_train[idx_ui], b_train[idx_vj])
            a_train[idx_ui] = np.copy(a_train[idx_ui] - eta*gradient_this_a)
            #update bj
            gradient_this_b = grad_b(U_train[idx_ui,:], Yij, V_train[idx_vj,:], reg, eta, a_train[idx_ui], b_train[idx_vj])
            b_train[idx_ui] = np.copy(b_train[idx_vj] - eta*gradient_this_b)
            
        error_t = get_err_bias(U_train, V_train, Y, a_train, b_train, reg)
        errores[i_epoch] = error_t
        eps_this = abs(error_t - error_tm1)/abs(error_one - error_zero)
        if debug:
            print("After epoch: "+str(i_epoch)+", error = "+str(error_t)+", eps = "+str(eps_this))
        if i_epoch > 1 and eps_this < eps:
            break
            
    error = get_err_bias(U_train, V_train, Y, a_train, b_train, reg)
        
    return U_train, V_train, a_train, b_train, error
