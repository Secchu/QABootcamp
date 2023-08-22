using ServerlessDictionary.Data;
using Microsoft.AspNetCore.Mvc;

namespace ServerlessDictionary.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class DictionaryController : ControllerBase
    {
        private readonly IDictionaryRepository<string, string> dictionary;

        public DictionaryController(IDictionaryRepository<string, string> dictionary)
        {
            this.dictionary = dictionary;
        }

        // GET: Dictionary/{key}
        [HttpGet("{key}")]
        public ActionResult<KeyValuePair<string, string>> Get(string key)
        {
            string value = dictionary.Find(key);

            if (value == null)
                return NotFound();

            var kv = new KeyValuePair<string, string>(key, value);

            return kv;
        }

        // GET: Dictionary/
        [HttpGet]
        public ActionResult<IEnumerable<KeyValuePair<string, string>>> GetAll()
        {
            return dictionary.GetAll().ToList();
        }

        // DELETE: Dictionary/{key}
        [HttpDelete("{key}")]
        public ActionResult<KeyValuePair<string, string>> Delete(string key)
        {
            if (!dictionary.TryDelete(key))
                return NotFound();

            return NoContent();
        }

        // PUT: Dictionary/{key}
        [HttpPut("{key}")]
        public ActionResult<KeyValuePair<string, string>> PutKeyValuePair(string key, KeyValuePair<string, string> kv)
        {
            if (!key.Equals(kv.Key))
                return BadRequest();

            if(!dictionary.TryUpdate(key, kv.Value))
                return BadRequest();

            return NoContent();
        }

        // POST: Dictionary/{key}
        [HttpPost]
        public ActionResult<KeyValuePair<string, string>> PostKeyValuePair(KeyValuePair<string, string> kv)
        {
            if (!dictionary.TryAdd(kv.Key, kv.Value))
                return BadRequest();

            return new ObjectResult(kv) { StatusCode = 201 };
        }

    }
}
