# openapi.api.DefaultApi

## Load the API package
```dart
import 'package:openapi/api.dart';
```

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**readRootGet**](DefaultApi.md#readrootget) | **GET** / | Read Root
[**updateItemItemsItemIdPut**](DefaultApi.md#updateitemitemsitemidput) | **PUT** /items/{item_id} | Update Item


# **readRootGet**
> Object readRootGet()

Read Root

### Example
```dart
import 'package:openapi/api.dart';

final api_instance = DefaultApi();

try {
    final result = api_instance.readRootGet();
    print(result);
} catch (e) {
    print('Exception when calling DefaultApi->readRootGet: $e\n');
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Object**](Object.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **updateItemItemsItemIdPut**
> Object updateItemItemsItemIdPut(itemId, item)

Update Item

### Example
```dart
import 'package:openapi/api.dart';

final api_instance = DefaultApi();
final itemId = 56; // int | 
final item = Item(); // Item | 

try {
    final result = api_instance.updateItemItemsItemIdPut(itemId, item);
    print(result);
} catch (e) {
    print('Exception when calling DefaultApi->updateItemItemsItemIdPut: $e\n');
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **itemId** | **int**|  | 
 **item** | [**Item**](Item.md)|  | 

### Return type

[**Object**](Object.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

