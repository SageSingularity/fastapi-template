# openapi.api.ItemsApi

## Load the API package
```dart
import 'package:openapi/api.dart';
```

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**readItemItemsItemIdGet**](ItemsApi.md#readitemitemsitemidget) | **GET** /items/{item_id} | Read Item


# **readItemItemsItemIdGet**
> Object readItemItemsItemIdGet(itemId, q)

Read Item

### Example
```dart
import 'package:openapi/api.dart';

final api_instance = ItemsApi();
final itemId = 56; // int | 
final q = q_example; // String | 

try {
    final result = api_instance.readItemItemsItemIdGet(itemId, q);
    print(result);
} catch (e) {
    print('Exception when calling ItemsApi->readItemItemsItemIdGet: $e\n');
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **itemId** | **int**|  | 
 **q** | **String**|  | [optional] 

### Return type

[**Object**](Object.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

